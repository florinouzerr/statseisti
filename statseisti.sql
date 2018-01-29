/*
CREATE DATABASE statseisti;
USE statseisti;
*/
DROP TABLE Accede;
DROP TABLE Fonction;
DROP TABLE Connexion;
DROP TABLE Utilisateur;
DROP TABLE Stage;
DROP TABLE SpecialiteCampus;
DROP TABLE Eleve;

CREATE TABLE Eleve(
	id VARCHAR(8) PRIMARY KEY,
	adresse VARCHAR(100),
	codePostal VARCHAR(10),
	ville VARCHAR(50),
	pays VARCHAR(50)
);

CREATE TABLE SpecialiteCampus(
	id INT PRIMARY KEY AUTO_INCREMENT,
	programme VARCHAR(20),
	campus VARCHAR(5),
	anneeScolaire VARCHAR(9),
	idEleve VARCHAR(8),
	FOREIGN KEY fk_eleve(idEleve) REFERENCES Eleve(id)
);

CREATE TABLE Stage(
	id INT PRIMARY KEY AUTO_INCREMENT,
	annee VARCHAR(10),
	anneeScolaire VARCHAR(9),
	entreprise VARCHAR(100),
	codePostal VARCHAR(10),
	ville VARCHAR(50),
	pays VARCHAR(50),
	sujet VARCHAR(2000),
	salaire INT,
	idEleve VARCHAR(8),
	FOREIGN KEY fk_eleve(idEleve) REFERENCES Eleve(id)
);

CREATE TABLE Utilisateur(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nom VARCHAR(50),
	prenom VARCHAR(100),
	mail VARCHAR(100),
	motDePasse VARCHAR(50),
	adresse VARCHAR(100),
	codePostal VARCHAR(10),
	ville VARCHAR(100),
	pays VARCHAR(50),
	telephone VARCHAR(10)
);

CREATE TABLE Connexion(
	id INT PRIMARY KEY AUTO_INCREMENT,
	adresseIP VARCHAR(16),
	systExploitation VARCHAR(50),
	dateDebut DATETIME,
	duree TIME,
	idUtilisateur INT,
	FOREIGN KEY fk_utilisateur(idUtilisateur) REFERENCES Utilisateur(id)
);

CREATE TABLE Fonction(
	id INT PRIMARY KEY AUTO_INCREMENT,
	libelle VARCHAR(20)
);

CREATE TABLE Accede(
	idUtilisateur INT,
	idFonction INT,
	CONSTRAINT pk_Accede PRIMARY KEY (idUtilisateur, idFonction),
	FOREIGN KEY fk_utilisateur(idUtilisateur) REFERENCES Utilisateur(id),
	FOREIGN KEY fk_fonction(idFonction) REFERENCES Fonction(id)
);


