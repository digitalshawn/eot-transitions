#!/usr/bin/env python

import os
import csv
import sys
import uuid
import json
import os.path
import requests
import argparse
import subprocess
from bs4 import BeautifulSoup
from simhash import Simhash, SimhashIndex

tmap = sys.argv[1]
final_result = sys.argv[2]
for_yuxu = sys.argv[3]
final_json = sys.argv[4]

# read the timemap
if os.path.isfile(tmap): 
	mementos = []
	with open(tmap, 'r') as f1:
		for m in f1:
			if m[-1:] == '\n':
				mementos.append(m[:-1])
else:
	print 'File name of the timemap "'+tmap+'" does not exist'
	sys.exit(0)

c0 = 0
c1 = 0
c2 = 0

lastlist = []
Taken = []
for m in mementos:
	c0 = c0 + 1
	#print m
	year = m[27:31]
	month = m[31:33]
	day = m[33:35]
	#print 'year=', year , ' month = ', month, ' day = ', day
	if (year in ['2001', '2005', '2009', '2013', '2017']) and (month in ['01','02','03']):
		c1 = c1 + 1 
		if (year+month+day) not in Taken:
			c2 = c2 + 1
			Taken.append(year+month+day)
			lastlist.append(m) 
			#print m
print
print ('{:6s}{:80s}'.format(str(c0), ' <--- Total mementos'))
print ('{:6s}{:80s}'.format(str(c1), ' <--- After filtering (years: 01, 05, 09, 13, 17)  and months (01, 02 ,03)'))
print ('{:6s}{:80s}'.format(str(c2), ' <--- More filtering  (One memento per day) \n'))

FIRST = True
cou = 0;
IDF = 0
Editd = 0

tmpNewFilename = './tmp/'+str(uuid.uuid4())+'_new'
tmpOldFilename = './tmp/'+str(uuid.uuid4())+'_old'

for uri in lastlist:
		try:
			r = requests.get(uri, timeout=1000,
            	                allow_redirects=True)
			r.raise_for_status()
		except Exception as e:
			#print str(cou) + '  ' +  str(e)
			continue;

		cou = cou + 1
		soup = BeautifulSoup(r.text,"html.parser")
		stext = soup.text
		#sim = Simhash(r.text)
		sim = Simhash(stext)
		#newText = r.text
		newText = stext

		if not FIRST:
			DIST = sim.distance(oldSim)
			with open(tmpNewFilename, "w") as tfi:
				tfi.write(newText.encode('ascii', 'ignore'))

			with open(tmpOldFilename, "w") as tfi:
				tfi.write(oldText.encode('ascii', 'ignore'))

			output = subprocess.check_output("python3 compare.py "+tmpOldFilename+"  "+tmpNewFilename, shell=True)
			IDF = output.strip()

		else:
			FIRST = False
			DIST = 0

		print ('{:4s} {:75s}  {:20s} {:3s} {:17s}'.format(str(cou), uri, str(sim.value) , str(DIST) , str(IDF)))

		with open(final_result, 'a') as f:
			f.write('{:4s} {:75s}  {:20s} {:3s} {:17s}\n'.format(str(cou), uri, str(sim.value) , str(DIST) , str(IDF)))

		year = uri[27:31]
		month = uri[31:33]
		day = uri[33:35]

		with open(for_yuxu, 'a') as f:
			writer = csv.writer(f)
			fields=[year,month,day, str(DIST) , str(IDF), str(Editd)]
			writer.writerow(fields)

		oldSim = sim
		oldText = newText

l = []

dd = {
  "cols": [{"id": "capture_date", "label": "date of capture", "type": "date"},
    {"id": "simhash", "label": "simhash diff", "type": "number"},
    {"id": "tfidf", "label": "TF/IDF", "type": "number"},
         {"id": "wburl", "label": "URL to Wayback capture", "type": "string"},
         {"id": "render_page", "label": "URL to render thumbnail", "type": "string"}
  ],
  "rows": []}

with open(final_result) as f:
    content = f.readlines()
content = [x.strip() for x in content] 


for c in content:
	y = c.split('http://web.archive.org/web/',1)[1][0:4]
	m = c.split('http://web.archive.org/web/',1)[1][4:6]
	d = c.split('http://web.archive.org/web/',1)[1][6:8]
	ttt = c.split('http://web.archive.org/web/',1)[1][0:14]
	dd['rows'].append({"c":[    
							 {"v": "Date("+y+","+m+","+d+")"   },
							 {"v": int(c.split()[3]) },
							 {"v": m+","+d+","+y},
							 {"v": "<a href=\""+c.split()[1]+"\"><img src=\"https://raw.githubusercontent.com/digitalshawn/eot-transitions/master/thumbnails/whitehouse/2017/thumb-whitehouse.gov-"+ttt+".png\" border=0></a>"}

					       ]   
					  }
					 )
#print dd
with open(final_json, 'w') as outfile:
     json.dump(dd, outfile, indent = 4)


os.remove(tmpNewFilename) 
os.remove(tmpOldFilename) 




