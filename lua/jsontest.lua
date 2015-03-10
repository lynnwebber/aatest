#!/usr/bin/env lua
--
local cjson = require('cjson')

local function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end

local inf = assert(io.open("aajson.json", "r"))

local hold = inf:read("*all")
inf:close()

local working = cjson.decode(hold)

print(dump(working))
