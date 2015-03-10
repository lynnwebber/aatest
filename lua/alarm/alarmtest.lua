#!/usr/bin/env lua
--
-----  globals -----
redis = require('redis')
clnt = redis.connect('127.0.0.1',6379)

--
--  talk to redis to get the value of the tagid
--
function get_reading(tagid)
    ky = "rdg:" .. tagid
    print(ky)
    t = clnt:get(ky)
    if t ~= nil then print("debug-reading " .. t) end
    return t
end

--
--  talk to redis to get the alarm code
--
function get_alarm(tagid)
    ky = "alrm:" .. tagid
    code = clnt:get(ky)
    if code ~= nil then print("debug-code " .. code) end
    return code
end

--
--  the following emulates incomming messages with tagid(s) that
--    have recently posted readings.  will ultimately come from
--    checking a topic on NSQ and possibly spawn off a coroutine
--
tlst = {'8.12119.1','8.12120.1','8.14662.1','8.23792.1','8.12179.1','10.1.1'}

for i,v in ipairs(tlst) do
    code = get_alarm(v)
    if code ~= nil then
        f = assert(loadstring(code))
        f()
        result = check_alarm()
        if result == 1 then
            print('*** ALARM *** for tag ' .. v)
        elseif result == 0 then
            print('normal for tag ' .. v)
        elseif result == 99 then
            print('reading not found for tag ' .. v)
        else
            print("unknow return value for alarm check " .. v)
        end
    else
        print('no alarm code for tag ' .. v)
    end
    print('-------\n\n')
end
