#from django.shortcuts import render
#from .forms import ContactForm

#def contact(request):
	# Construire le formulaire, soit avec les données postées,
	# soit vide si l'utilisateur accède pour la première fois
	# à la page.
#	form = ContactForm(request.POST or None)
	# Nous vérifions que les données envoyées sont valides
	# Cette méthode renvoie False s'il n'y a pas de données 
	# dans le formulaire ou qu'il contient des erreurs.
#	if form.is_valid():
		# Ici nous pouvons traiter les données du formulaire
#		suject = form.cleaned_data['subject']
#		message = form.cleaned_data['message']
#		envoyeur = form.cleaned_data['envoyeur']
#		renvoi = form.cleaned_data['renvoi']

		# Nous pourrions ici envoyer l'e-mail grâce aux données 
		# que nous venons de récupérer
#		envoi = True
	
	# Quoiqu'il arrive, on affiche la page du formulaire.
#	return render(request, 'nous_contacter/contact.html', locals())


# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['florin.gogibus78100@gmail.com']) #Le mail sera envoyé à florin.gogibus78100@gmail.com
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect(successView)
	return render(request, "nous_contacter/email.html", {'form': form})

def successView(request):
   return HttpResponse('Success! Thank you for your message.')

