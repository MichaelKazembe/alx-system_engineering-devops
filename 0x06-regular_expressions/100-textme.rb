#!/usr/bin/env ruby
string = ARGV[0].scan(/\[from:(.*?)\]|\[to:(.*?)\]|\[flags:(.*?)\]/).join(" ")
string = string.squeeze(' ')
list = string.split
puts list.join(',')
