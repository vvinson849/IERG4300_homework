#!/usr/bin/env python
import sys
from collections import defaultdict
from itertools import combinations

s = 0.005

baskets = []
for basket in sys.stdin :
	baskets.append(basket.strip())
support = len(baskets) * s

item_count = defaultdict(lambda: 0)
for basket in baskets :
	for item in basket.split() :
		item_count[item] += 1
cand_items = [item for item in item_count if item_count[item] >= support]

pair_count = defaultdict(lambda: 0)
for basket in baskets :
    basket = [item for item in basket.split() if item in cand_items]
    for pair in combinations(basket, 2) :
        pair_count[tuple(sorted(pair))] += 1
cand_pairs = [pair for pair in pair_count if pair_count[pair] >= support]

triplet_count = defaultdict(lambda: 0)
for basket in baskets :
	basket = basket.split()
	for triplet in combinations(basket, 3) :
		for pair in combinations(triplet, 2) :
			if tuple(sorted(pair)) not in cand_pairs : break
		else :
			triplet_count[tuple(sorted(triplet))] += 1                 

for triplet in triplet_count :
	if triplet_count[triplet] >= support :
		print("{triplet}	{count}".format(triplet=' '.join(triplet), count=triplet_count[triplet]))
