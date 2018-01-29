from django.db import models


class Accede(models.Model):
    idutilisateur = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idUtilisateur', primary_key=True)  # Field name made lowercase.
    idfonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='idFonction')  # Field name made lowercase.



class Connexion(models.Model):
    adresseip = models.CharField(db_column='adresseIP', max_length=16, blank=True, null=True)  # Field name made lowercase.
    systexploitation = models.CharField(db_column='systExploitation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datedebut = models.DateTimeField(db_column='dateDebut', blank=True, null=True)  # Field name made lowercase.
    duree = models.TimeField(blank=True, null=True)
    idutilisateur = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idUtilisateur', blank=True, null=True)  # Field name made lowercase.



class Eleve(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    adresse = models.CharField(max_length=100, blank=True, null=True)
    codepostal = models.CharField(db_column='codePostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50,null=True)
    latitude = models.CharField(max_length=50,null=True)

class Fonction(models.Model):
    libelle = models.CharField(max_length=20, blank=True, null=True)

    

class Specialitecampus(models.Model):
    programme = models.CharField(max_length=20, blank=True, null=True)
    campus = models.CharField(max_length=25, blank=True, null=True)
    anneescolaire = models.CharField(db_column='anneeScolaire', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ideleve = models.ForeignKey(Eleve, models.DO_NOTHING, db_column='idEleve', blank=True, null=True)  # Field name made lowercase.



class Stage(models.Model):
    annee = models.CharField(max_length=150, blank=True, null=True)
    anneescolaire = models.CharField(db_column='anneeScolaire', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entreprise = models.CharField(max_length=100, blank=True, null=True)
    codepostal = models.CharField(db_column='codePostal', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    sujet = models.CharField(max_length=3000, blank=True, null=True)
    salaire = models.CharField(max_length=10,blank=True, null=True)
    ideleve = models.ForeignKey(Eleve, models.DO_NOTHING, db_column='idEleve', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)



class Pays(models.Model):
    pays = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)




class Utilisateur(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    motdepasse = models.CharField(db_column='motDePasse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(max_length=100, blank=True, null=True)
    codepostal = models.CharField(db_column='codePostal', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ville = models.CharField(max_length=100, blank=True, null=True)
    pays = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)




