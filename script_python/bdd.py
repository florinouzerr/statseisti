import re
filename = './files/ADR_ELEVES_2017_2018_DATA_TABLE_ANO.txt'
i = 0
donnees = []
print("Fichier en cours de traitement : ",filename)
for line in open(filename,'r', encoding='latin-1'):
	donnees.append(line.split("\t"))
	print(line.split("\t"))
print("Nombre de lignes dans le fichier",len(donnees))
