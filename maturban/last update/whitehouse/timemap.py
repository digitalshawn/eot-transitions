#!/usr/bin/env python

import csv   


import requests
from simhash import Simhash, SimhashIndex
import sys


import subprocess




import requests
import argparse
import os

r = requests.get('http://web.archive.org/web/timemap/link/'+'https://www.whitehouse.gov', timeout=1000,
                            allow_redirects=True)  

mementos = []
for m in r.content.split('\n'):
	if ('rel="memento";' in m) and (('http://web.archive.org/web/' in m) or ('https://web.archive.org/web/' in m)):
		m.replace('https:','http:')
		uri =  'http:' + m.split('http:',1)[1].split('>')[0]
		ttime =  uri.split('web.archive.org/web/')[1][0:14]
		uri = uri.replace(ttime,ttime+'id_')
		mementos.append(uri)

# # remove this for the final version
# f1=open('./tm.txt', 'w')
# c = 0
# for m in mementos:
# 	c = c + 1
# 	if c == 1: 
# 		f1.write(m)
# 	else:
# 		f1.write('\n'+m)	
# f1.close()


# # read from file remove this for the final version
# mementos = []
# with open('./tm.txt', 'r') as f1:
# 	for m in f1:
# 		if m[-1:] == '\n':
# 			mementos.append(m[:-1])




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

for uri in lastlist:
		try:
			r = requests.get(uri, timeout=1000,
            	                allow_redirects=True)
			r.raise_for_status()
		except Exception as e:
			#print str(cou) + '  ' +  str(e)
			continue;

		cou = cou + 1
		sim = Simhash(r.text)
		newText = r.text


		if not FIRST:
			DIST = sim.distance(oldSim)
			with open("new", "w") as tfi:
				tfi.write(newText.encode('ascii', 'ignore'))

			with open("old", "w") as tfi:
				tfi.write(oldText.encode('ascii', 'ignore'))

			output = subprocess.check_output("python3 compare.py old new ", shell=True)
			IDF = str(output.split(" ")[0]).strip()
			Editd = str(output.split(" ")[1]).strip()

		else:
			FIRST = False
			DIST = 0

		print ('{:4s} {:75s}  {:20s} {:3s} {:17s} {:6s}'.format(str(cou), uri, str(sim.value) , str(DIST) , str(IDF), str(Editd)))

		with open('result.txt', 'a') as f:
			f.write(('{:4s} {:75s}  {:20s} {:3s} {:17s} {:6s} \n'.format(str(cou), uri, str(sim.value) , str(DIST) , str(IDF), str(Editd))))

		year = uri[27:31]
		month = uri[31:33]
		day = uri[33:35]
		#print year, month, day, str(DIST) , str(IDF), str(Editd) 


		with open(r'res.csv', 'a') as f:
			writer = csv.writer(f)
			fields=[year,month,day, str(DIST) , str(IDF), str(Editd)]
			writer.writerow(fields)

		# if FIRST:
		# 	FIRST = False
		# 	#print '%4s %' % str(cou) + '  ' + uri + '   ' + str(sim.value) 
		# 	print '{:4s} {:78s}  {:20s} {:3s} {:3s}'.format(str(cou), uri, str(sim.value), '-' , '0' )
		# 	oldSim = sim
		# else:
		# 	if sim.value == oldSim.value:
		# 		#print str(cou) + '  ' + uri + '   ' + str(sim.value) 
		# 		print '{:4s} {:78s}  {:20s} {:3s} {:3s}'.format(str(cou), uri, str(sim.value), '-' , str(DIST) )
		# 	else:
		# 		print '{:4s} {:78s}  {:20s} {:3s} {:3s}'.format(str(cou), uri, str(sim.value), '**' , str(DIST) )
		# 		#print str(cou) + '  ' + uri + '   ' + str(sim.value) + ' Dist = ' + str(DIST)  + '         ***'
		
		oldSim = sim
		oldText = newText







