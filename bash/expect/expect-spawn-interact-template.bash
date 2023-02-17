#!/usr/bin/expect -f
set timeout -1
spawn ##CMD##
expect -exact ""
send -- "\r" ## do not remove \r at the end
expect "*" 
send -- "\r" ## do not remove \r at the end
interact