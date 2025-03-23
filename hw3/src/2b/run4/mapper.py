#!/usr/bin/env python3
import sys
import numpy as np

centroids = None
with open("part-00000") as f :
	centroids = [np.array(list(map(float, vector.split(',')))) for vector in f.readlines()]

for line in sys.stdin :
	pt = np.array(list(map(float, line.split(','))))
	dists = [np.linalg.norm(pt - centroid) for centroid in centroids]
	print("{nearest_centroid},{vector}".format(
		nearest_centroid = dists.index(min(dists)),
		vector = line))
