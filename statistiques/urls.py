from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from statistiques import views

app_name = 'statistiques'
urlpatterns = [
	url(r'^menu_stats$', views.menu_stats, name='menu_stats'),
	url(r'^uni_programme$', views.uni_programme, name='uni_programme'),
	url(r'^quali_quali$',views.quali_quali, name ='quali_quali'),
	url(r'^uni_eleves$',views.uni_eleves, name ='uni_eleves'),
	url(r'^result$',views.result, name ='result'),
	url(r'^money_stage$',views.money_stage, name ='money_stage'),
	url(r'^best_stage$',views.best_stage, name ='best_stage'),

]



