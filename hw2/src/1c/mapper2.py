#!/usr/bin/env python
import sys
from collections import defaultdict

candidate_triplets = None
with open("part-00000") as f :
	candidate_triplets = [tuple(triplet.strip().split()) for triplet in f.readlines()]

triplet_count = defaultdict(lambda: 0)
for basket in sys.stdin :
	basket = basket.strip().split()
	for triplet in candidate_triplets :
		if triplet[0] in basket and triplet[1] in basket and triplet[2] in basket :
			triplet_count[triplet] += 1

for triplet in triplet_count :
	print("{triplet}	{count}".format(triplet=' '.join(triplet), count=triplet_count[triplet]))
