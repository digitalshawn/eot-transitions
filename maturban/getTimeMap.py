#!/usr/bin/env python

import sys
import time
import requests

def download_file(url):
    # NOTE the stream=True parameter
    mems = ''
    r = requests.get(url, stream=True)
    #with open('temp__map.txt', 'w') as f:
    for chunk in r.iter_content(chunk_size=1024): 
        print chunk
        if chunk:
            mems += chunk
    return mems

url = sys.argv[1]
fname = sys.argv[2]
print 'url: ', url

#r = requests.get('http://web.archive.org/web/timemap/link/'+url, stream=True, allow_redirects=True)  
mems = download_file('http://web.archive.org/web/timemap/link/'+url)

print 'Writing to a file ... '

mementos = []
#for m in r.content.split('\n'):
for m in mems.split('\n'):
    print m
    if ('rel="memento";' in m) and (('http://web.archive.org/web/' in m) or ('https://web.archive.org/web/' in m)):
        m.replace('https:','http:')
        uri =  'http:' + m.split('http:',1)[1].split('>')[0]
        ttime =  uri.split('web.archive.org/web/')[1][0:14]
        uri = uri.replace(ttime,ttime+'id_')
        mementos.append(uri)

# remove this for the final version
f1=open(fname, 'w')
c = 0
for m in mementos:
  c = c + 1
  if c == 1: 
      f1.write(m)
  else:
      f1.write('\n'+m)    
f1.close()

print '\n The TimeMap was stored in '+ fname + '\n'
