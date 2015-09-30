#!/usr/bin/ruby -w
#
require 'bcrypt'

print "hashtest\n"

a_password = BCrypt::Password.create("toddflaska@1")
print a_password, "\n"

printf "version %s\n", a_password.version
printf "cost %s\n", a_password.cost
printf "is it 'secret' %s\n", a_password == "toddflaska@1"
printf "is it 'stuff' %s\n", a_password == "stuff"
