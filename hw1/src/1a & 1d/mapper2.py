#!/usr/bin/env python
import sys

for line in sys.stdin:
	line = line.strip().split()
	referee = int(line[0])
	referrer_list = list(map(int, line[1:]))

	for i in range(len(referrer_list)):
		for j in range(len(referrer_list)):
			if i == j : continue
			print("{referrer1} {referrer2}	{referee1}".format(
					referrer1 = referrer_list[i],
					referrer2 = referrer_list[j],
					referee1 = referee )
			)

