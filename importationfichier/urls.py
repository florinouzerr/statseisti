from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from importationfichier import views

app_name = 'importefichier'
urlpatterns = [
	url(r'^upload$', views.upload, name='upload'),
	url(r'^nouveau_document$', views.nouveau_document, name='nouveau_document'),
	url(r'^import_bdd$', views.import_bdd, name='import_bdd'),
	url(r'^import_bdd/(\d+)$',views.upload_bdd,name='upload_bdd'),
	url(r'^delete_file/(\d+)$',views.delete_file,name='delete_file'),
	url(r'^delete_base_eleve$',views.delete_base_eleve,name='delete_base_eleve'),
	url(r'^delete_base_stage$',views.delete_base_stage,name='delete_base_stage'),
	url(r'^delete_base_programme$',views.delete_base_programme,name='delete_base_programme'),

]

