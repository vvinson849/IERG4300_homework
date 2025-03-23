#!/usr/bin/env python
import sys
from operator import itemgetter

last_referrer = None
referee_list = []

for line in sys.stdin :
	line = line.strip().split()
	cur_referrer = line[0]
	cur_referee = line[1]

	if cur_referrer == last_referrer :
		referee_list.append(cur_referee)
	else :
		if last_referrer is not None:
			print("{web1}	{web_list}".format(
				web1 = last_referrer,
				web_list = ' '.join(referee_list)
				)
			)
		last_referrer = cur_referrer
		referee_list = [cur_referee]

print("{web1}	{web_list}".format(
	web1 = last_referrer,
	web_list = ' '.join(referee_list)
	)
)

