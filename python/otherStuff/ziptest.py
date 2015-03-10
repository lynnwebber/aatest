#!/usr/bin/python
#

import os, sys
import zipfile
from translate.misc import zipfileext

m = md5.md5()
m.update('lynnwebber@somervillepartners.com')
res = m.hexdigest()
print '{',res,'}'

print len(res)
