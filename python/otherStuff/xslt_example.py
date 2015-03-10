#! /usr/bin/env python

import time
st = time.time()

import libxml2, libxslt
import cgi, os, sys

query = cgi.FieldStorage()

readtimestart = time.time()
styledoc = libxml2.parseFile("page.xsl")
style = libxslt.parseStylesheetDoc(styledoc)
doc = libxml2.parseFile(query['script'].value)
readtimeend = time.time()


start_converting = time.time()
result = style.applyStylesheet(doc, None)
done_converting = time.time()

html = result.serialize()

print "Content-type: text/html"
print
print html

style.freeStylesheet()
doc.freeDoc()
result.freeDoc()

et = time.time()
totaltime = et-st
print "<!-- Page served in %s seconds. -->" % totaltime
print "<!-- XML conversion took %s seconds. -->" %\
(done_converting-start_converting)
print "<!-- File reading took %s seconds. -->" %\
(readtimeend-readtimestart)

