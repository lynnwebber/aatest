#!/usr/bin/python
# 

import config as cfg
import os, sys
import subprocess
import SocketServer

# ----------------------------------------------------------
def daemonize_old():
    # a very basic version of the double fork method of creating
    #   a disconnected process
    # fork off a sub process
    if os.fork() != 0:
        os._exit(0)

    # create a session and set the process group ID
    os.setsid()

    if os.fork() != 0:
        os._exit(0)

    os.chdir("/")
    os.umask(022)
    # close 0-stdin, 1-stdout, 2-stderr 
    [os.close(i) for i in xrange(3)]
    
    os.open(os.devnull, os.O_RDWR)
    os.dup2(0, 1)
    os.dup2(0, 2)


# ----------------------------------------------------------
def daemonize():
    """ Detach a process from the controlling terminal session and
    run it in the background (what unix calls a daemon)
    """
    try:
        # fork a child process so the parent can exit and setup a
        #   process that can become the session leader without an
        #   attached terminal
        pid = os.fork()
    except OSError, e:
        raise Exception "%s [%d]" % (e.strerror, e.errno)
    if (pid == 0): # from the first forked child
        # use setsid to become the session leader and
        #   guarantee that there is no controlling terminal
        os.setsid()
        try:
            # now fork a second child and exit to prevent zombies
            #   the second child will be orphaned.  This child is
            #   no longer a session leader preventing it from ever
            #   getting a controlling terminal
            pid = os.fork()
        except OSError, e:
            raise Exception, "%s [%d]" % (e.strerror, e.errno)

        if (pid == 0):  # from the second child
            # change to the root directory so we avoid the
            #   issue of not being able to unmount stuff at shutdown
            #   time
            os.chdir("/")
            # now specifically set the file mode creation mask to
            #   give the child complete control over the permissions
            os.umask(022)
        else:
            os._exit(0)
    else:
        os._exit(0)

    # close standard file descriptiors 0-stdin, 1-stdout, 2-stderr 
    [os.close(i) for i in xrange(3)]

    # this call to open is guaranteed to grab the lowest file descriptor
    #   which will be 0 (stdin) because it was closed above
    os.open(os.devnull, os.O_RDWR)
    # now duplicate the standard input to stdout and stderr
    os.dup2(0, 1)
    os.dup2(0, 2)
    # and now the rest of the code will run in the detached process
 
# ----------------------------------------------------------
class Handler(SocketServer.StreamRequestHandler):

    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break
            self.wfile.write("you sent: %s" % (data,))


# ----------------------------------------------------------
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True
    pass

# ----------------------------------------------------------------
def main(args):
    daemonize()
    srvr = ThreadedTCPServer((cfg.service.host,cfg.service.port),Handler)
    try:
        srvr.serve_forever()
    except KeyboardInterrupt:
        pass

# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__":
    sys.exit(main(sys.argv))
