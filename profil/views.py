from django.shortcuts import render ,get_object_or_404

from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import EditProfilForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group
from accueil_login.views import home
from django.contrib.auth.models import User, Group

def user_profil(request):
	if request.method == "POST":
		form = User(request.POST)
		if form.is_valid():
			post = form.save
			post.author = request.user
			post.save()
			return redirect('profil/pageprofil')
	else:  
		form = User()
		return render(request, 'profil/editprofil.html', {'form': form})

def edit_user(request):
	if not request.user.is_authenticated :
		return redirect(pageprofil)	 
	return render(request, 'profil/pageprofil.html', locals())

	

def pageprofil(request): 
	
	if request.user.is_authenticated :
		user = User.objects.get(pk=request.user.id)	
		if request.method == 'POST':
			form = EditProfilForm(request.POST, instance=request.user)

			if form.is_valid():
				form.save()
				return redirect('profil:pageprofil')
			return render(request, 'profil/pageprofil.html')
		else:
			form = EditProfilForm(instance=request.user)
			args = {'form': form, 'user' : user.username}
			return render(request, 'profil/pageprofil.html', args)

		
	else :
		return redirect(home)

	
