#!/usr/bin/env python

import requests
from simhash import Simhash, SimhashIndex
import sys

r = requests.get('http://web.archive.org/web/timemap/link/'+'https://www.whitehouse.gov', timeout=1000,
                            allow_redirects=True)  
# mementos = []
# for m in r.content.split('\n'):
# 	if ('rel="memento";' in m) and (('http://web.archive.org/web/' in m) or ('https://web.archive.org/web/' in m)):
# 		m.replace('https:','http:')
# 		uri =  'http:' + m.split('http:',1)[1].split('>')[0]
# 		ttime =  uri.split('web.archive.org/web/')[1][0:14]
# 		uri = uri.replace(ttime,ttime+'id_')
# 		mementos.append(uri)

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


# read from file remove this for the final version
mementos = []
with open('./tm.txt', 'r') as f1:
	for m in f1:
		if m[-1:] == '\n':
			mementos.append(m[:-1])
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
			print m
print c0
print c1
print c2

# sys.exit(0)

FIRST = True
cou = 0;
for uri in lastlist:
		cou = cou + 1
		try:
			r = requests.get(uri, timeout=1000,
            	                allow_redirects=True)
			r.raise_for_status()
		except Exception as e:
			print str(cou) + '  ' +  str(e)
			continue; 

		sim = Simhash(r.text)

		if not FIRST:
			DIST = sim.distance(oldSim)
		if FIRST:
			FIRST =False
			print str(cou) + '  ' + uri + '   ' + str(sim.value)
			oldSim = sim
		else:
			if sim.value == oldSim.value:
				print str(cou) + '  ' + uri + '   ' + str(sim.value) 
			else:
				print str(cou) + '  ' + uri + '   ' + str(sim.value) + ' Dist = ' + str(DIST)  + '         ***'
			oldSim = sim







