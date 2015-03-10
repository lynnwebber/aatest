#!/usr/bin/env lua
--
-----  globals -----
i = 2000

--
-- in production this function would talk to redis
--   to get the most current value of the tag that was passed
--
function get_value(tagid)
    t = math.random()+math.random(1,20)
    print("value " .. t)
    return t
end


---- local code to run ----
local inf = assert(io.open("alarmcode.lua", "r"))
local code = inf:read("*all")
inf:close()

f = assert(loadstring(code))

f()
for i=1,45 do
    if check_alarm() == 1 then
        print('alarm')
    else
        print("all ok")
    end

end
