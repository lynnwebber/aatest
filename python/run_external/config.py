#!/usr/bin/env python

class opt:
    gen_filename=True
    remove_previous=True
    verbose=True


class fn:
	fn_seed="cdot_ldap"
	ftype=".csv"


class pull:
    cmd='csvde -s hqdc4.dot.state.co.us  -n -f cdotldapexport.csv -r "(&(mail=*)(!(objectclass=contact)))"'


class prev:
	remove_fn="*.csv"


class ftp:
    host="gawhaq.state.co.us"
    user="rcole"
    pwd="t1pt0p4u"

