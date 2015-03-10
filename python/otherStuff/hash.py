#!/usr/bin/python
#

import os, sys
import hashlib

for arg in sys.argv[1:]:
    m = hashlib.md5()
    m.update(arg)
    x = m.hexdigest()
    print "%s -->  %s" % (arg,x)

