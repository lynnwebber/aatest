#!/usr/bin/python
#

import os
import inputParser as ireq
import dataProcessing as dp
import subManager as sm

xmlstr = ''
fobj = open('../testing/zin1.xml','r')

for line in fobj:
    xmlstr += line.strip()
fobj.close()

if ireq.reqdata.parse(xmlstr):
    z = dp.gen_outstream()
else:
    print "didnt parse"

sm.run_sub(z)

