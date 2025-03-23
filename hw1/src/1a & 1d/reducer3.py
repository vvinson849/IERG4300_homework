#!/usr/bin/env python
from operator import itemgetter
import sys

last_referrer1 = None
min_referrer2 = None
max_list = []
max_size = 0

for line in sys.stdin:
	line = line.strip().split()
	cur_referrer1 = int(line[0])
	cur_referrer2 = int(line[1])
	cur_list = list(map(int, line[2:]))
	cur_size = len(cur_list)

	if cur_referrer1 == last_referrer1:
		if cur_size > max_size or (cur_size == max_size and cur_referrer2 < min_referrer2):
			min_referrer2 = cur_referrer2
			max_list = cur_list
			max_size = cur_size
	else:
		print("{web1}:{web2}, {open_bracket}{web_list}{close_bracket}, {size}".format(
			web1 = last_referrer1,
			web2 = min_referrer2,
			open_bracket = '{',
			web_list = ','.join(map(str, max_list)),
			close_bracket = '}',
			size = max_size )
		)
		last_referrer1 = cur_referrer1
		min_referrer2 = cur_referrer2
		max_list = cur_list
		max_size = cur_size

print("{web1}:{web2}, {open_bracket}{web_list}{close_bracket}, {size}".format(
	web1 = last_referrer1,
	web2 = min_referrer2,
	open_bracket = '{',
	web_list = ','.join(map(str, max_list)),
	close_bracket = '}',
	size = max_size )
)

