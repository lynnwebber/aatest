#!/usr/bin/python
#

import os
import xmlrpclib

url='http://localhost:31033/'
s = xmlrpclib.ServerProxy(url)

xmlstr = ''
fobj = open('zin1.xml','r')

for line in fobj:
    xmlstr += line.strip()
fobj.close()

print s.sendHubMsg(xmlstr)

#print s.ServiceVerify()