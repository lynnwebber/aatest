#!/usr/bin/python

import xmlrpclib, code

#url='http://localhost:31033'
url='http://soa001.somervillepartners.com:31033'
s = xmlrpclib.ServerProxy(url)

print "Hint: Use s.system.listMethods() to see whats available"

interp = code.InteractiveConsole({'s': s})
interp.interact("Use the object s to interact with the server.")

