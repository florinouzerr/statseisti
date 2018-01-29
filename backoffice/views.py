from django.shortcuts import render, get_object_or_404
from .models import Utilisateur

def index(request):
    user_list = Utilisateur.objects.all()
    context = {'user_list': user_list,}
    return render(request,'backoffice/index.html',context)

def user(request, user_id):
	user_tmp = get_object_or_404(Utilisateur,pk=user_id)
	return render(request,'backoffice/user.html',{'user_tmp' : user_tmp})

