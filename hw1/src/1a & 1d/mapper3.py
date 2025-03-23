#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip().split()
	referrer1 = int(line[0])
	referrer2 = int(line[1])
	referee_list = list(map(int, line[2:]))
	print("{web1} {web2}	{web_list}".format(
		web1 = referrer1,
		web2 = referrer2,
		web_list = ' '.join(map(str, referee_list)) )
	)

