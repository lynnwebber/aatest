#!/usr/bin/python
#

import md5, time

def mkguid():

    m = md5.md5()
    m.update('lynnwebber@somervillepartners.com')
    res = m.hexdigest()
    print '{',res,'}  length->',len(res)

