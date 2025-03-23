#!/usr/bin/env python
import sys
from collections import defaultdict
from itertools import combinations

candidate_pairs = None
with open("part-00000") as f :
	candidate_pairs = [tuple(pair.strip().split()) for pair in f.readlines()]

pair_count = defaultdict(lambda: 0)
for basket in sys.stdin :
	basket = basket.strip().split()
	for pair in combinations(basket, 2) :
		pair = tuple(sorted(pair))
		if pair in candidate_pairs :
			pair_count[pair] += 1

for pair in pair_count :
	print("{pair}	{count}".format(pair=' '.join(pair), count=pair_count[pair]))
