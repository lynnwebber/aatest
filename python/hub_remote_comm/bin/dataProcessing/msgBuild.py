#!/usr/bin/env python
# 

import inputParser as ireq

def gen_outstream():

    rv = ''
    tmp = []
    tgt = ireq.reqdata.target

    # pull target data out of input request
    ip = tgt['ip_address']
    cmt = tgt['comments']
    typ = tgt['comm_type'].lower()
    
    # determine the request type and build the tuples
    #    with the appropriate data for the child process
    #    and put them in an array that can be turned into a string
    if typ == "modbus_write":
        mb = ireq.reqdata.mbwrite
        tmp.append(('ip',ip))
        tmp.append(('slv',mb['slave_id']))
        tmp.append(('fnc',mb['function_code']))
        tmp.append(('addr',mb['output_address']))
        tmp.append(('val',mb['output_value']))

        # now turn it into a string formatted with ":" separators
        #  and "|" for variable breaks using some fun array stuff
        rv = '|'.join([x+":"+y for x,y in tmp])
   
    # will return empty string if not a valid type
    return rv

    
    
    
# ----------------------------------------------------------------
# main program module
#
def msgBuild_main():
    print "child process message building module"


# ----------------------------------------------------------------
#  run main
#
if __name__ == "__main__": msgBuild_main()
