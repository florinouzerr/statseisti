from backoffice.models import *
import os
import csv
i = 0
s = Stage.objects.all()
tmp = os.getcwd() +"/media/documents/geo_stage.txt.geocoded.csv"
cr = csv.reader(open(tmp,'r'))
for e,f in zip(s,cr):
	e.latitude = f[0]
	e.longitude = f[1]
	e.save()
	print(i)
	print(e.latitude)
	print(e.longitude)
	i = i +1

from backoffice.models import *
import os
import csv
i = 0
s = Eleve.objects.all()
tmp = os.getcwd() +"/media/documents/geo_adr.txt.geocoded.csv"
cr = csv.reader(open(tmp,'r'))
for e,f in zip(s,cr):
	e.latitude = f[0]
	e.longitude = f[1]
	e.save()
	print(i)
	print(e.latitude)
	print(e.longitude)
	i = i +1

from backoffice.models import *
import os
import csv
i = 0
oss = []
tmp = os.getcwd() +"/media/documents/geo_adr.txt.geocoded.csv"
cr = csv.reader(open(tmp,'r'))
for f in cr:
	try :
		oss.append((float((f[0])),float(f[1])))
		print(i)
		i = i +1
	except:
		i = i + 0





