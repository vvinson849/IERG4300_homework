#!/usr/bin/env python
from operator import itemgetter
import sys

last_referrer1 = None
last_referrer2 = None
referee_list = []

for line in sys.stdin:
	line = line.strip().split()
	cur_referrer1 = int(line[0])
	cur_referrer2 = int(line[1])
	cur_referee = int(line[2])

	if last_referrer1 == cur_referrer1 and last_referrer2 == cur_referrer2:
		referee_list.append(cur_referee)
	else:
		if last_referrer1 is not None and last_referrer2 is not None:
			print("{web1} {web2}    {web_list}".format(
				web1 = last_referrer1,
				web2 = last_referrer2,
				web_list = ' '.join(map(str, referee_list)) )
			)
		last_referrer1 = cur_referrer1
		last_referrer2 = cur_referrer2
		referee_list = [cur_referee]

#if last_referrer1 == cur_referrer1 and last_referrer2 == cur_referrer2:
print("{web1} {web2}    {web_list}".format(
	web1 = last_referrer1,
	web2 = last_referrer2,
	web_list = ' '.join(map(str, referee_list)) )
)

