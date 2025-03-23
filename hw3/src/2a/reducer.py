#!/usr/bin/env python3
from operator import itemgetter
import sys
import numpy as np

cur_centroid = None
last_centroid = None
last_centroid_vec = np.zeros(784)
num_vector = None
for line in sys.stdin:
    try:
        # Strip leading/trailing whitespace and split by comma
        line = line.strip().split(',')
        
        # Ensure the line has at least 2 elements (centroid ID and vector values)
        if len(line) < 2:
            continue

        # Convert the first element to an integer (centroid ID)
        cur_centroid = int(line[0])

        # Convert the rest of the line into a NumPy array (vector)
        cur_pt = np.array(list(map(float, line[1:])))
    except (ValueError, IndexError):
        # Skip lines that are empty, invalid, or improperly formatted
        continue
    
    if cur_centroid == last_centroid :
        last_centroid_vec += cur_pt
        num_vector += 1  
    else :
        if last_centroid is not None :
            print(','.join(map(str, last_centroid_vec/num_vector)))
        last_centroid = cur_centroid
        last_centroid_vec = cur_pt
        num_vector = 1

if last_centroid == cur_centroid and num_vector > 0 :
    print(','.join(map(str, last_centroid_vec/num_vector)))
