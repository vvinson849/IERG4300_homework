#!/usr/bin/env python
from operator import itemgetter
import sys

s = .01
num_basket = int(sys.argv[1])
support = s * num_basket

cur_pair = None
last_pair = None
cur_count = 0
last_count = 0
for line in sys.stdin :
	line = line.strip().split()
	cur_pair = (line[0], line[1])
	cur_count = int(line[2])
	if cur_pair != last_pair :
		if last_pair is not None and last_count >= support :
			print("{pair}	{count}".format(pair=' '.join(last_pair), count=last_count))
		last_pair = cur_pair
		last_count = cur_count
	else :
		last_count += cur_count

if cur_pair == last_pair and last_count >= support :
	print("{pair}	{count}".format(pair=' '.join(last_pair), count=last_count))
