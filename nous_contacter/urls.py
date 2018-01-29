from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from nous_contacter import views

#app_name = 'nous_contacter'
#urlpatterns = [
#	url(r'^contact$', views.contact, name='contact'),
#]


# sendemail/urls.py
urlpatterns = [
	url(r'^email/$', views.emailView, name='email'),
	url(r'^success/$', views.successView, name='success'),
    #path('email/', views.emailView, name='email'),
    #path('success/', views.successView, name='success'),
]