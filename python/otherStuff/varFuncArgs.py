#!/usr/bin/python
#

import md5, time
import random

def doboth(name,email):
    m = md5.md5()
    m.update(name)
    m.update(email)
    res = m.hexdigest()
    print "full:",res
 
def doname(name):
    m = md5.md5()
    m.update(name)
    res = m.hexdigest()
    print "name only:",res   


doboth('lynn webber','lwebber@somervillepartners.com')
doname('lynn webber')
