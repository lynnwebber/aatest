#!/usr/bin/python
#

x = 100.0 / 16.0
print x
for i in range(0,16,3):
    if i > 0:
        z = (float(i) * x) / 100
    else:
        z = i
    msg = '%d --> %s --> %.2f' % (i,hex(i),z)
    print msg
