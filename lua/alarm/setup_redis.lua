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
talrm = [[
function check_alarm()
    val=get_reading("8.12119.1")
    if val == nil then
        return 99
    end
    if tonumber(val) > 10.2 then
        return 1
    else
        return 0
    end
end
]]
clnt:set('alrm:8.12119.1',talrm)

talrm = [[
function check_alarm()
    val=get_reading("8.12120.1");
    if val == nil then
        return 99
    end
    if tonumber(val) > 12.5 then
        return 1
    else
        return 0
    end;
end
]]
clnt:set('alrm:8.12120.1',talrm)

talrm = [[
function check_alarm()
    val=get_reading("8.14662.1");
    if val == nil then
        return 99
    end
    if tonumber(val) > 10.2 then
        return 1
    else
        return 0
    end;
end
]]
clnt:set('alrm:8.14662.1',talrm)

talrm = [[
function check_alarm()
    val=get_reading("10.1.1");
    if val == nil then
        return 99
    end
    if tonumber(val) > 10.2 then
        return 1
    else
        return 0
    end;
end
]]
clnt:set('alrm:10.1.1',talrm)
