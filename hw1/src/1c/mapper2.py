#!/usr/bin/env python
import sys

for line in sys.stdin :
	line = line.strip().split()
	referee = line[0]
	referrer_list = line[1:]
	print("{web1}	{web_list}".format(
		web1 = referee, web_list = ' '.join(referrer_list))
	)
