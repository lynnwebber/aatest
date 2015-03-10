#!/usr/bin/env python

import sys, time
from detached_process import DetachedProcess

class aDetachedProcess(detached_process):
    def run(self):
        while True:
            time.sleep(1)

if __name__ == "__main__":
    dp = aDetachedProcess('/tmp/detached_process_test.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            dp.start()
        elif 'stop' == sys.argv[1]:
            dp.stop()
        elif 'restart' == sys.argv[1]:
            dp.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
