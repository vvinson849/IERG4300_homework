#!/usr/bin/env python
import sys

for line in sys.stdin :
	line = line.strip().split()
	print("{web1}	{web2}".format(
		web1 = line[0],
		web2 = line[1])
	)

