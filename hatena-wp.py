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
    new_line = "DATE: " + year + "/" + month + "/" + day + "\n"
  else:
    new_line = line

  sys.stdout.write(new_line)
  line = f.readline()
f.close
