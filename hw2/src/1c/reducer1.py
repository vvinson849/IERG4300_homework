#!/usr/bin/env python
from operator import itemgetter
import sys

last_triplet = None
for line in sys.stdin :
	line = line.strip().split()
	cur_triplet = (line[0], line[1], line[2])
	if cur_triplet != last_triplet :
		print(' '.join(cur_triplet))
	last_triplet = cur_triplet
