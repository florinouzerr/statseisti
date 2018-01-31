from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from backoffice.models import *
from accueil_login.views import home

import json
import itertools
import random
import os
import csv

# Create your views here.

def hex_code_colors(): #fontion qui permet de creer des couleurs aléatoirement
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()


def menu_stats(request):
    if request.user.is_active:
        return render(request, 'statistiques/index.html')
    else :
        return redirect(home)   



def uni_programme(request):
    if request.user.is_active:
        donnees_campus = []
        donnees_annee_scolaire = []
        color_campus = []
        color_annee_scolaire = []
        labels_campus = []
        labels_annee_scolaire = []
        val_list_campus = []
        val_list_annee_scolaire = []
        val_list_programme= []
        val_int_campus = []
        val_int_annee_scolaire = []

        labels_bdd_campus = Specialitecampus.objects.values('campus').distinct()
        labels_bdd_annee_scolaire = Specialitecampus.objects.values('anneescolaire').distinct().order_by('anneescolaire')   

    
        for tmp in labels_bdd_campus:
            labels_campus.append(tmp['campus'].replace("\n",""))
            val_int_campus.append(Specialitecampus.objects.filter(campus = tmp['campus']).values('ideleve').distinct().count())
            color_campus.append(hex_code_colors())

        for tmp in labels_bdd_annee_scolaire:
            labels_annee_scolaire.append(tmp['anneescolaire'].replace("\n",""))
            val_int_annee_scolaire.append(Specialitecampus.objects.filter(anneescolaire = tmp['anneescolaire']).values('ideleve').distinct().count())
            color_annee_scolaire.append(hex_code_colors())

        somme_campus = sum(val_int_campus)
        
        for tmp in val_int_campus:
            donnees_campus.append(round(tmp / somme_campus,2)*100)

        for tmp in val_int_annee_scolaire:
            donnees_annee_scolaire.append(tmp)

        for tmp,tmp_bis in zip(labels_campus,val_int_campus):
            val_list_campus.append("Nombre d'élève à " + tmp + " : " + str(tmp_bis))

        

        donnees_campus.append(0)
        donnees_annee_scolaire.append(0)

        return render(request, 'statistiques/uni_programme.html',{
            'total_cergy' : val_list_campus[0],
            'total_pau' : val_list_campus[1],
            'donnees_campus':donnees_campus,
            'donnees_annee_scolaire' : donnees_annee_scolaire,
            'labels_campus' : labels_campus,
            'labels_annee_scolaire' : labels_annee_scolaire,
            'total_eleve' : somme_campus,
            'var_list_campus':val_list_campus,
            'var_list_annee_scolaire' : val_list_annee_scolaire,
            'color_campus' : color_campus,
            'color_annee_scolaire' : color_annee_scolaire,
            'labels_annee_scolaire' : labels_annee_scolaire,})
        return redirect(home)
    else :
        return redirect(home)   

def quali_quali(request) :
    if request.user.is_active:
        color_programme_ING = []
        color_programme_CPI = []
        labels_annee_scolaire = []
        labels_programme_ING = []
        labels_programme_CPI = []
        labels_annee_scolaire = []
        val_list_annee_scolaire = []
        val_list_programme= []
        val_int_campus = []
        val_int_annee_scolaire = []
        val_int_programme_ING = []
        val_int_programme_CPI = []

        labels_bdd_annee_scolaire = Specialitecampus.objects.values('anneescolaire').distinct().order_by('anneescolaire')   
        labels_bdd_programme_ING = (Specialitecampus.objects.filter(programme__startswith='ING')).values('programme').distinct().order_by('programme')
        labels_bdd_programme_CPI = (Specialitecampus.objects.filter(programme__startswith='CPI')).values('programme').distinct().order_by('programme')

        for annee in labels_bdd_annee_scolaire:
            labels_annee_scolaire.append(annee['anneescolaire'].replace("\n",""))


        for prog in labels_bdd_programme_ING:
            labels_programme_ING.append(prog['programme'].replace("\n",""))

        for prog in labels_bdd_programme_CPI:
            labels_programme_CPI.append(prog['programme'].replace("\n",""))

        for tmp in labels_bdd_annee_scolaire:
            tmp_valeur = []
            tmp_couleur = []
            for prog in labels_bdd_programme_ING:
                tmp_valeur.append((Specialitecampus.objects.filter(programme = prog['programme']) & Specialitecampus.objects.filter(anneescolaire = tmp['anneescolaire'])).values('ideleve').distinct().count())
                tmp_couleur.append(hex_code_colors())
            val_int_programme_ING.append(tmp_valeur)
            color_programme_ING.append(tmp_couleur)

        for tmp in labels_bdd_annee_scolaire:
            tmp_valeur = []
            tmp_couleur = []
            for prog in labels_bdd_programme_CPI:
                tmp_valeur.append((Specialitecampus.objects.filter(programme = prog['programme']) & Specialitecampus.objects.filter(anneescolaire = tmp['anneescolaire'])).values('ideleve').distinct().count())
                tmp_couleur.append(hex_code_colors())
            val_int_programme_CPI.append(tmp_valeur)
            color_programme_CPI.append(tmp_couleur)
        


        liste_ING = zip(val_int_programme_ING,color_programme_ING)
        liste_CPI = zip(val_int_programme_CPI,color_programme_CPI)
        return render(request, 'statistiques/quali_quali.html',{
            'labels_annee_scolaire' : labels_annee_scolaire,
            'labels_programme_ING' :labels_programme_ING,
            'labels_programme_CPI' : labels_programme_CPI,
            'liste_ING':liste_ING,
            'liste_CPI': liste_CPI})
        return redirect(home)
    else :
        return redirect(home)   

def uni_eleves(request) :
    if request.user.is_active:
        i = 0
        val_int_pays = []
        labels_pays = []
        pays_gps = []
        color_pays = []
        labels_pays_trunc = []
        val_int_pays_trunc = []
        val_int_pays_tmp = []
        labels_bdd_pays = Eleve.objects.values('pays').distinct()
        labels_bdd_ville = Eleve.objects.values('ville').distinct().order_by('vile')    


        oss_lon = []
        oss_lat = []
        tmp = os.getcwd() +"/media/documents/geo_adr.txt.geocoded.csv"
        cr = csv.reader(open(tmp,'r'),delimiter=',')
        for f in cr:
            try :
                oss_lat.append(float(f[0]))
                oss_lon.append(float(f[1]))
                print(i)
                i = i +1
            except:
                i = i + 0


        i = 0

        for tmp in labels_bdd_pays:
            labels_pays.append(tmp['pays'].replace("\n",""))
            
            val_int_pays.append(Eleve.objects.filter(pays = tmp['pays']).values('id').distinct().count())
            color_pays.append(hex_code_colors())

        val_int_pays_tmp = sorted(zip(val_int_pays, range(len(val_int_pays))),reverse = True)
        print(val_int_pays_tmp)
        for val in val_int_pays_tmp: 
            labels_pays_trunc.append(labels_pays[val_int_pays_tmp[i][1]])
            if (tmp != None):
                print("111")
            val_int_pays_trunc.append(val_int_pays_tmp[i][0])
            i = i +1
        val_int_pays.append(0)
        return render(request, 'statistiques/uni_eleves.html',{
            'labels_pays' : labels_pays_trunc,
            'val_int_pays' : val_int_pays_trunc,
            'color_pays' : color_pays,
            'oss_lat' : oss_lat,
            'oss_lon' : oss_lon
            })
        return redirect(home)
    else :
        return redirect(home)   

def calculdistance(point1,point2):
    return(vincenty(point1, point2).miles*1.60934)

def result(request):
    if request.user.is_active:
        return render(request, 'statistiques/results.html')
    else :
        return redirect(home)   

def money_stage(request):
    i = 0
    if request.user.is_active:
        val_bdd_ing1 = []
        bdd_ing1 = Stage.objects.filter(annee='ING1')
        val_bdd_ing2 = []
        bdd_ing2 = Stage.objects.filter(annee='ING2')
        val_bdd_ing3 = []
        bdd_ing3 = Stage.objects.filter(annee='ING3')


        for x in bdd_ing1:
            try :
                val_bdd_ing1.append(float(x.salaire.replace(',','.')))
            except:
                i = i +1
        salaire_ing1 = sum(val_bdd_ing1) / len(val_bdd_ing1)

        for x in bdd_ing2:
            try :
                val_bdd_ing2.append(float(x.salaire.replace(',','.')))
            except:
                i = i +1
        salaire_ing2 = sum(val_bdd_ing2) / len(val_bdd_ing2)

        for x in bdd_ing3:
            try :
                val_bdd_ing3.append(float(x.salaire.replace(',','.')))
            except:
                i = i +1
        salaire_ing3 = sum(val_bdd_ing3) / len(val_bdd_ing3)
        return render(request, 'statistiques/money_stage.html',{
            'salaire_ing1' :round(salaire_ing1,2),
            'salaire_ing2' :round(salaire_ing2,2),
            'salaire_ing3' :round(salaire_ing3,2)})
    else :
        return redirect(home)


def best_stage(request):
    i = 0
    if request.user.is_active:
        """
        labels_entreprise_trunc = []
        bdd_stage = Stage.objects.values('entreprise').distinct()
        val_int_entreprise = []
        label_stage = []
        labels_entreprise = []
        val_int_entreprise_tmp = []
        for x in bdd_stage:
            label_stage.append(x)
    
        
        for tmp in label_stage:
            labels_entreprise.append(tmp['entreprise'])
        
        for x in labels_entreprise:
            val_bdd_entreprise = []
            bdd_entreprise = Stage.objects.filter(entreprise=x)
            print("ok")
            print(bdd_entreprise)
            for x in bdd_entreprise:
                try :
                    val_bdd_entreprise.append(float(x.salaire.replace(',','.')))
                except:
                    i = i +1
            try :   
                val_int_entreprise.append(sum(val_bdd_entreprise) / len(val_bdd_entreprise))
            except:
                i = i +1

        val_int_entreprise_tmp = sorted(zip(val_int_entreprise, range(len(val_int_entreprise))),reverse = True)[0:5]
        print(val_int_entreprise_tmp)
        for val in val_int_entreprise_tmp: 
            labels_entreprise_trunc.append(labels_entreprise[val_int_entreprise_tmp[i][1]])
            val_int_entreprise_trunc.append(val_int_entreprise_tmp[i][0])
            i = i +1"""
        return render(request, 'statistiques/best_stage.html')
    else :
        return redirect(home)
