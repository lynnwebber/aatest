#!/usr/bin/python
#

import os
import dimscores as ds
import calc
import cache

xmlstr = ''
fobj = open('../testing/zin1.xml','r')
#fobj = open('../testing/zin2.xml','r')


for line in fobj:
    xmlstr += line.strip()
fobj.close()

ds.xml.parse(xmlstr)
calc.calc_factors()
calc.calc_styles()

z = cache.gen_outstream()
print z

cache.debug.purge()
cache.score.purge()

