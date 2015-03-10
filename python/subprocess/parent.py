#!/usr/bin/env python
import os, sys
import subprocess 
import time

for i in range(5):
    subprocess.Popen(["python","hello.py","ip:127.0.0.1|type:MODBUS|reg:13453|typ:4|val:0X044401"])

print "parent still going"
time.sleep(4)
print "parent ending"
sys.exit(0)