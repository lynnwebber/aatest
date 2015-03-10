import os, sys
import time 

print "hello - child started: ",os.getpid()
print "received: ",sys.argv[1]
time.sleep(1)
print "child ended: ",os.getpid()
sys.exit()
