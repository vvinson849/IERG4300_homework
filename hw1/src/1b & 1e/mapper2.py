#!/usr/bin/env python
import sys

for line in sys.stdin :
	line = line.strip().split()
	referrer = line[0]
	referees = line[1:]
	print("{web1}	{web_list}".format(
		web1 = referrer,
		web_list = ' '.join(referees) )
	)
