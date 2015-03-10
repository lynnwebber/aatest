#!/usr/bin/python

import xmlrpclib, code

#url='http://localhost:31033'
url='http://155.229.187.12:44821'
s = xmlrpclib.ServerProxy(url)

print "Hint: Use s.system.listMethods() to see whats available"

interp = code.InteractiveConsole({'s': s})
interp.interact("Use the object s to interact with the server.")

