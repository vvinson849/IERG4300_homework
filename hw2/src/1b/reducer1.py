#!/usr/bin/env python
from operator import itemgetter
import sys

last_pair = None
for line in sys.stdin :
	line = line.strip().split()
	cur_pair = (line[0], line[1])
	if cur_pair != last_pair :
		print(' '.join(cur_pair))
	last_pair = cur_pair
