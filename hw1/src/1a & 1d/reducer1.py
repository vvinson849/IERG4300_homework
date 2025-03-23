#!/usr/bin/env python
from operator import itemgetter
import sys

referrer_list = []
last_referee = None

for line in sys.stdin:
	line = line.strip().split()
	cur_referee = int(line[0])
	cur_referrer = int(line[1])

	if cur_referee == last_referee:
		referrer_list.append(cur_referrer)
	else:
		if last_referee is not None:
			print("{web1}   {web2}".format(web1=last_referee, web2=' '.join(map(str, referrer_list))))
		last_referee = cur_referee
		referrer_list = [cur_referrer]

#if cur_referee == last_referee :
print("{web1}	{web2}".format(web1=last_referee, web2=' '.join(map(str, referrer_list))))

