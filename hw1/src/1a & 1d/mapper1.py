#!/usr/bin/env python
import sys

for line in sys.stdin:
        line = line.strip().split()
        referrer = int(line[0])
        referee = int(line[1])
        print("{web1}   {web2}".format(web1=referee, web2=referrer))
