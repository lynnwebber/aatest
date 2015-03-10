#!/usr/bin/env python

import sys, os, time, atexit
from signal import SIGTERM 

class DetachedProcess:
    """
    A generic detached process class.  Sometimes called a daemon in unix.
    Usage: subclass the detached process class and override the run() method
    """
    # --------------------------------------------------------
    def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    # --------------------------------------------------------
    def detach_process(self):
        """
        do the UNIX double-fork magic, see Stevens' -Advanced 
        Programming in the UNIX Environment- for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit first parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/") 
        os.setsid() 
        os.umask(0) 

        # do second fork
        try: 
            pid = os.fork() 
            if pid > 0:
                # exit from second parent
                sys.exit(0) 
        except OSError, e: 
            sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
            sys.exit(1) 

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # write pidfile
        atexit.register(self.delpid)
        pid = str(os.getpid())
        file(self.pidfile,'w+').write("%s\n" % pid)
	
    # --------------------------------------------------------
    def delpid(self):
        os.remove(self.pidfile)

    # --------------------------------------------------------
    def start(self):
        """
        Start the detached process
        """
        # Check for a pidfile to see if the process is already running
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Process already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the detached process
        self.detach_process()
        self.run()

    # --------------------------------------------------------
    def status(self):
        """
        Give Status of detached process
        """
        # Check for a pidfile to see if the process is running
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if pid:
            message = "%s                             running - Pid:%d\n" % (sys.argv[0],pid)
            sys.stderr.write(message)
            sys.exit(1)
        else:
            message = "%s                             not running\n" % (sys.argv[0])
            sys.stderr.write(message)
            sys.exit(1)
            
    # --------------------------------------------------------
    def stop(self):
        """
        Stop the detached process
        """
        # Get the pid from the pidfile
        try:
            pf = file(self.pidfile,'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Process not running?\n"
            sys.stderr.write(message % self.pidfile)
            return # not an error in a restart

        # Try killing the process	
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
                message = "%s                             Stopped\n" % (sys.argv[0])
                sys.stderr.write(message)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print str(err)
                sys.exit(1)

    # --------------------------------------------------------
    def restart(self):
        """
        Restart the detached process
        """
        self.stop()
        self.start()

    # --------------------------------------------------------
    def run(self):
        """
        You should override this method when you subclass a detached process.
        It will be called after the process has been detached by start() or restart().
        """
