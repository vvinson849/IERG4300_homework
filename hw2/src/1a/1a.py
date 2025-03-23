from collections import defaultdict
from itertools import combinations

s = .01
baskets = []

with open("yelp_review_50000_100000") as f :
    baskets = [basket.strip() for basket in f.readlines()]
support = len(baskets) * s

item_count = defaultdict(lambda: 0)
for basket in baskets :
    for item in basket.split() :
        item_count[item] += 1
freq_items = [item for item in item_count if item_count[item] >= support]

pair_count = defaultdict(lambda: 0)
for basket in baskets :
    basket = [item for item in basket.split() if item in freq_items]
    for pair in combinations(basket, 2) :
        pair_count[tuple(sorted(pair))] += 1

for pair in pair_count :
    if pair_count[pair] >= support :
        print(' '.join(pair), pair_count[pair])
