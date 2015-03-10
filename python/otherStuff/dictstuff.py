#!/usr/bin/python
#

import md5, time
import random

m = md5.md5()
m.update('lynnwebber@somervillepartners.com')
res = m.hexdigest()
print '{',res,'}'

print len(res)