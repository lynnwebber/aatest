#!/usr/bin/env lua
--
--

local inf = assert(io.open(arg[1], "r"))
local outf = assert(io.open("junk.txt", "w"))


for ln in inf:lines() do
    outf:write(ln,"\n")
end

inf:close()
outf:close()
