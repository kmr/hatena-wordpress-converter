#!/usr/bin/python
# coding: UTF-8

import sys
import re

date_pattern = re.compile ('^DATE: (.+?)/(.+?)/(.+?) (.+?):(.+?):(.+?) (.+?)$')

f = open(sys.argv[1])
line = f.readline()
while line:
  new_line = ""
  m = date_pattern.match(line)
  if m:
    year = m.group(3)
    month = m.group(1)
    day = m.group(2)
    hour = m.group(4)
    minute = m.group(5)
    sec = m.group(6)
    ampm = m.group(7)
    if ampm == "AM":
      ampm = ""
    else:
      ampm = " PM"

    new_line = "DATE: " + year + "/" + month + "/" + day + " " + hour + ":" + minute + ":" + sec + ampm + "\n"
  else:
    new_line = line

  sys.stdout.write(new_line)
  line = f.readline()
f.close
