#!/usr/bin/env lua
--
redis = require('redis')
clnt = redis.connect('127.0.0.1',6379)

-- load some readings
clnt:set('rdg:8.12119.1',8.2245)
clnt:set('rdg:8.12120.1',15.62)
clnt:set('rdg:8.14662.1',225.36)
clnt:set('rdg:8.23792.1',24.3)
clnt:set('rdg:8.12179.1',46.257)

-- load some alarm functions

clnt:set('alrm:8.12119.1','function check_alarm () val=get_value("8.12119.1"), if val > 10.2 then return 1 else return 0 end')
clnt:set('alrm:8.12120.1','function check_alarm () val=get_value("8.12120.1"), if val > 12.5 then return 1 else return 0 end')
clnt:set('alrm:8.14662.1','function check_alarm () val=get_value("8.14662.1"), if val > 10.2 then return 1 else return 0 end')
