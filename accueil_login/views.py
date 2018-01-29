from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, ConnexionForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def home(request):
	error = False

	if request.method == "POST":
		print("okokokoko")
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			print(user)

			if user:  # Si l'objet renvoyé n'est pas None
				print("ok")                
				login(request, user)  # nous connectons l'utilisateur
				return redirect(hello)
			  #return render(request, 'accueil_login/hello.html')
			else: # sinon une erreur sera affichée
				print("pasco")
				error = True
	else:
		form = ConnexionForm()

	if request.user.is_authenticated:
		return redirect(hello)

	return render(request, 'accueil_login/home.html', locals())

def apropos(request):
	return render(request, 'accueil_login/apropos.html', locals())
	
def hello(request):
	if not request.user.is_authenticated :
		return redirect(home)
	else :
		return render(request, 'accueil_login/hello.html', locals())

#def home(request):
	#return render(request, 'accueil_login/home.html')
	#return render(request, 'accueil_login/index.html')


def deconnexion(request):
	logout(request)
	return render(request, 'accueil_login/home.html', locals())


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activer votre compte Stats Eisti.'
			message = render_to_string('accueil_login/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
						mail_subject, message, to=[to_email]
			)
			email.send()
			return render(request, 'accueil_login/message_inscription.html', locals())
			#return HttpResponse(tmp)
	else:
		form = SignupForm()
	return render(request, 'accueil_login/signup.html', {'form': form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		# return redirect('home')
		return render(request, 'accueil_login/merci.html', locals())
	else:
		return HttpResponse("Le lien d'activation est invalide !")






