#!/usr/bin/env python
from operator import itemgetter
import sys

s = .005
num_basket = int(sys.argv[1])
support = s * num_basket

cur_triplet = None
last_triplet = None
cur_count = 0
last_count = 0
for line in sys.stdin :
	line = line.strip().split()
	cur_triplet = (line[0], line[1], line[2])
	cur_count = int(line[3])
	if cur_triplet != last_triplet :
		if last_triplet is not None and last_count >= support :
			print("{triplet}	{count}".format(triplet=' '.join(last_triplet), count=last_count))
		last_triplet = cur_triplet
		last_count = cur_count
	else :
		last_count += cur_count

if cur_triplet == last_triplet and last_count >= support :
	print("{triplet}	{count}".format(triplet=' '.join(last_triplet), count=last_count))
