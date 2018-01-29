from django.urls import include, path
from django.contrib import admin


urlpatterns = [
	path('nous_contacter/', include('nous_contacter.urls')),
    path('accueil_login/', include('accueil_login.urls')),
    #path('importationfichier/', include('importationfichier.urls')),
    path('backoffice/', include('backoffice.urls')),
    path('admin/', admin.site.urls),
    path('statistiques/', include('statistiques.urls')),
    path('importationfichier/', include('importationfichier.urls',namespace='importationfichier')),
	path('profil/', include('profil.urls')),
]
