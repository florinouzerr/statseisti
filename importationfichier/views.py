from django.shortcuts import render, redirect
from django.shortcuts import render_to_response 
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from importationfichier.models import Document
from backoffice.models import *
from accueil_login.views import home
from django.contrib.auth.models import User, Group

from .forms import *
import os, os.path, string 
from os.path import basename
import csv

def rechercheListe(liste,elt):
	for x in liste:
		if x == elt:
			return(True)
	return(False)


def nouveau_document(request):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)

	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff :
			form = UploadFileForm(request.POST or None, request.FILES)
			return render(request, 'importationfichier/home.html', {
				'form': form
				})
		return redirect(home)
	else :
		return redirect(home)


def upload(request):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			form = UploadFileForm(request.POST or None, request.FILES)
			request.session['sauvegarde'] = False
			document = Document()
			if form.is_valid():
				document.description = form.cleaned_data["title"]
				document.file = form.cleaned_data["file"]
				document.importer = False
				#if os.path.splitext(str)[1] == '.txt':
				if document.file :
					document.save()
					request.session['sauvegarde'] = True
			else :
				document.file = None
			return render(request, 'importationfichier/upload.html', { 'name_file': document.file })
		return redirect(home)
	else :
		return redirect(home)

def import_bdd(request):
	i = 0 # accumulateur
	docs = Document.objects.all()
	request.session['nbr_fichier_bdd'] = False
	request.session['nbr_fichier_serveur'] = False
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			while i < len(docs) :
				if docs[i].importer :
					request.session['nbr_fichier_bdd'] = True
					print(i)
				else :
					request.session['nbr_fichier_serveur'] = True
				i = i + 1
			print(i)
			print(request.session['nbr_fichier_serveur'])
			print(request.session['nbr_fichier_bdd'])
			return render(request, 'importationfichier/importbdd.html',{ 'document' : docs})
		return redirect(home)
	else :
		return redirect(home)


def upload_bdd(request,id_file):
	import os
	docs = Document.objects.get(pk=id_file)
	request.session['importation_bdd'] = False
	request.session['nbr_ligne_erreur_bdd'] = False
	file_name = "media/" + str(docs.file)
	i = 0 # itterateur pour le nombre de ligne dans le fichier
	donnees = [] # permet de stocker les valeurs du fichier dans un tableau de tableau
	donnees_brutes = [] # permet de stocker les valeurs du fichier dans un tableau ce sont des lignes
	ligne_erreurs = []
	fileName, fileExtension = os.path.splitext(basename(file_name))
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			#IMPORTATION FICHIER TXT

			if docs.importer == 0 and fileExtension == '.txt':
				fichier =  open(file_name,'r', encoding='cp1252')
				head = fichier.readline()


			#IMPORTATION FICHIER ADDRESSE ELEVES
				if file_name.lower().find("adr") >= 0:
					print("okkkjlkjk")
					print("okkkk")
					for line in fichier:
						donnees.append(line.split("\t"))
						donnees_brutes.append(line)
						try : 
							print(line)
							Eleve(adresse="NULL",
								id=donnees[i][3].replace("\n",""),
								codepostal=donnees[i][0],
								ville = donnees[i][1],
								pays=donnees[i][2]).save()
						except :
							donnees_brutes.append(line)
							request.session['nbr_ligne_erreur_bdd'] = True
							ligne_erreurs.append("Ligne " + str(i+1) + " : " +line)
						i = i + 1
					print("Nombre de lignes dans le fichier",i)
					docs.importer = True
					request.session['importation_bdd'] = True
					docs.save()
					return render(request, 'importationfichier/uploadbdd.html', { 'documents': docs ,'ligne_erreurs' :ligne_erreurs, 'donnees' : donnees_brutes})

			#IMPORTATION FICHIER STAGES

				if file_name.lower().find("stage") >= 0:
					print("okkkk")

					for line in fichier:
						donnees.append(line.split("\t"))
						print("caca",len(donnees[i][8].replace("\n","")))
						print("caca2",(donnees[i][8].replace("\n","")))
						print("en cours",i)
						tmp = Eleve.objects.get(pk=donnees[i][8].replace("\n",""))
						try : 
							tmp = Eleve.objects.get(pk=donnees[i][8].replace("\n",""))
							Stage(
								annee=donnees[i][0],
								anneescolaire=donnees[i][1],
								entreprise=donnees[i][2],
								codepostal=donnees[i][3],
								ville = donnees[i][4],
								pays=donnees[i][5],
								sujet=donnees[i][6],
								salaire=donnees[i][7],
								ideleve =tmp).save()
						except :
							donnees_brutes.append(line)
							request.session['nbr_ligne_erreur_bdd'] = True
							ligne_erreurs.append("Ligne " + str(i+1) + " : " +line)
						i = i + 1
					print("Nombre de lignes dans le fichier",i)
					docs.importer = True
					request.session['importation_bdd'] = True
					docs.save()

			#IMPORTATION FICHIER PROGRAMMES

				if file_name.lower().find("prg") >= 0:
					print("okkkk")
					for line in fichier:
						donnees.append(line.split("\t"))
						print("en cours",i)
						try : 
							tmp = Eleve.objects.get(pk=donnees[i][0].replace("\n",""))
							Specialitecampus(
								ideleve=tmp,
								programme=donnees[i][1],
								campus=donnees[i][3],
								anneescolaire=donnees[i][2]).save()
						except :
							donnees_brutes.append(line)
							request.session['nbr_ligne_erreur_bdd'] = True
							ligne_erreurs.append("Ligne " + str(i+1) + " : " +line)
						i = i + 1
					print("Nombre de lignes dans le fichier",i)
					docs.importer = True
					request.session['importation_bdd'] = True
					docs.save()

			#IMPORTATION FICHIER CSV

			if docs.importer == 0 and fileExtension == '.csv':
				if file_name.lower().find("adr") >= 0:
					fichier =  open(file_name,'rt', encoding='cp1252')
					reader = csv.reader(fichier)
					for ligne in reader:
						del ligne[4] #supprime le dernier element de la liste
						if i != 0:
							Eleve(adresse="NULL",
								id=ligne[3],
								codepostal=ligne[0],
								ville = ligne[1],
								pays=ligne[2]).save()
						
							donnees_brutes.append(ligne)
							request.session['nbr_ligne_erreur_bdd'] = True
							ligne_erreurs.append("Ligne " + str(i+1) + " : " + " ".join(ligne))
						i = i + 1
					print("Nombre de lignes dans le fichier",i)
					docs.importer = True
					request.session['importation_bdd'] = True
					docs.save()

				if file_name.lower().find("prg") >= 0:
					fichier =  open(file_name,'rt', encoding='cp1252')
					reader = csv.reader(fichier)
					for ligne in reader:
						print("nem : ",i)
						 #supprime le dernier element de la liste
						if i != 0:
							print(ligne)
							tmp = Eleve.objects.get(pk=ligne[0])
							Specialitecampus(
								ideleve=tmp,
								programme=ligne[1],
								campus=ligne[3],
								anneescolaire=ligne[2]).save()
						
							donnees_brutes.append(ligne)
							request.session['nbr_ligne_erreur_bdd'] = True
							ligne_erreurs.append("Ligne " + str(i+1) + " : " + " ".join(ligne))
						i = i + 1
					print("Nombre de lignes dans le fichier",i)
					docs.importer = True
					request.session['importation_bdd'] = True
					docs.save()
			return redirect(home)
	else :
		return redirect(home)

	return render(request,'importationfichier/uploadbdd.html', { 'documents': docs ,'ligne_erreurs' :ligne_erreurs, 'donnees' : donnees_brutes})

def delete_file(request,id_file):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			try :
				docs = Document.objects.get(pk=id_file)
				os.remove(docs.file.path)
				docs.delete()
				request.session['delete_file'] = True
			except:
				docs = None
				request.session['delete_file'] = False
			return render(request, 'importationfichier/delete_file.html',{'docs' : docs})
		return redirect(home)
	else :
		return redirect(home)

def delete_base_eleve(request):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			try :
				Eleve.objects.all().delete()
				request.session['delete_base'] = True
			except:
				request.session['delete_base'] = False
			return render(request, 'importationfichier/delete_base.html',{'nom' : "élèves"})
		return redirect(home)
	else :
		return redirect(home)

def delete_base_stage(request):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			try :
				Stage.objects.all().delete()
				request.session['delete_base'] = True
			except:
				request.session['delete_base'] = False
			return render(request, 'importationfichier/delete_base.html',{'nom' : "stage"})
		return redirect(home)
	else :
		return redirect(home)
def delete_base_programme(request):
	list_user_group = []
	user = User.objects.filter(groups__name='Gestionnaire_de_donnees')
	for tmp in user:
		list_user_group.append(tmp.id)
	if request.user.is_authenticated :
		if rechercheListe(list_user_group,request.user.id) or request.user.is_staff:
			try :
				Specialitecampus.objects.all().delete()
				request.session['delete_base'] = True
			except:
				request.session['delete_base'] = False
			return render(request, 'importationfichier/delete_base.html',{'nom' : "programmes"})
		return redirect(home)
	else :
		return redirect(home)	
