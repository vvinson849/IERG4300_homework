#!/usr/bin/env python
import sys
from operator import itemgetter

community_map = {}
results = {}

with open("medium_label") as f :
	for line in f.readlines() :
		line = line.strip().split()
		wid = int(line[0])
		cid = int(line[1])
		community_map[wid] = cid
		results[cid] = 0

for line in sys.stdin :
	line = line.strip().split()
	referee = int(line[0])
	referrer_list = list(map(int, line[1:]))
	if len(referrer_list) >= 2 :
		cid = community_map[referee]
		results[cid] += 1

for cid, count in results.items() :
	print("Community {comm}: {num}".format(comm = cid, num = count))
