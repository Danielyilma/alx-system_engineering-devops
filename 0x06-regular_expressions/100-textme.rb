#!/usr/bin/env ruby
result = ARGV[0].scan(/from:([+\w]*).*to:([+0-9]*).*flags:([(-1|0):]+)/)
puts result[0][0] + ", " + result[0][1] + ", " + result[0][2]
