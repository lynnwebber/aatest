#!/usr/bin/python
#

import os
import xmlrpclib

url='http://soa001.somervillepartners.com:31033/'
s = xmlrpclib.ServerProxy(url)

xmlstr = ''
fobj = open('zin2.xml','r')

for line in fobj:
    xmlstr += line.strip()
fobj.close()

print s.scoreFactors(xmlstr)

#print s.ServiceVerify()
