#!/usr/bin/python
#
####
# sample uuid generation methods for python
#   3 different ways
#  1) roll your own
#  2) standard library in python v2.5 (and above).  Can be found at http://zesty.ca/python/ for python v2.3 or v2.4
#  3) If on unix (whith uuidgen) installed use the uuidgen command
####

# ---------------------------------- example 1 roll your own -----------------------------
# Opinion: most flexable but has a very very very... small chance of generating a duplicate,
#          possibly a little slow due to the socket call,
#          very portable
#
import time, socket
import random, md5


def gen_uuid_1(*args):
    """
    Generates a UUID.
    Call with: any arguments, all arguments that are passed get added to the digest thus
      making the ID even more random
    Returns: a uuid string
    """
    rv = ''
    dgst = str(args)
    dgst += str(long(time.time()*1024))
    dgst += str(long( random.random() * 10000000000000000L) )
    try:
        addr = socket.gethostbyname(socket.gethostname())
    except:
        addr = ( random.random()*random.random() ) * 1000000000000000000L
    dgst += str(addr)
    rv = md5.md5(dgst).hexdigest()
    return rv


# ---------------------------------- example 2 python std library -----------------------------
# (see notes above for restrictions)
# Opinion: best choice if you are using python 2.3 or above and best for sure if you are using
#          python 2.5+.  Most portable, and has python community support.
#
import uuid

def gen_uuid_2():
    """
    Generates a UUID.
    Call with: nothing
    Returns: a uuid string
    Note:  See the documentation at http://zesty.ca/python/uuid.html for information on the
      different options and how to use.  I would recommend using the uuid4() method to
      generate a random UUID compliant with the RFC 4122 standard
    """
    rv = uuid.uuid4()
    return str(rv)


# ---------------------------------- example 3 unix uuidgen command -------------------------
# (see notes above for restrictions)
# Opinion:  Least portable and requires that uuidgen is installed on unix (although it is
#           there by default on most).  Probably the slowest because it has to fork another
#           process to run the command
#
import commands

def gen_uuid_3():
    """
    Generates a UUID.
    Call with: nothing
    Returns: a uuid string
    Note:  See unix uuidgen man page for options (not many)
    """
    return commands.getoutput('uuidgen')




print "\nGenerating UUID from the 'roll your own' algorithm example 1"
m = gen_uuid_1('lynn@neopsy.com')
print 'guid:',m
print 'length',len(m)

print "\nGenerating UUID from the 'python std lib' module  example 2"
m = gen_uuid_2()
print 'guid:',m
print 'length',len(m)

print "\nGenerating UUID from unix uuidgen command  example 3"
m = gen_uuid_3()
print 'guid:',m
print 'length',len(m)



