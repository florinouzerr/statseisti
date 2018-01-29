from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from profil import views

app_name = 'profil'
urlpatterns = [
	url(r'^user_profil$', views.user_profil, name='user_profil'),
	url(r'^editprofil$',views.user_profil, name="editprofil"),
	url(r'^pageprofil$', views.pageprofil, name='pageprofil'),

]
