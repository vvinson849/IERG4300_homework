#!/usr/bin/env python3
import os
import numpy as np
from collections import defaultdict

# K-means initialisation
np.random.seed(4300)

rand_indices = np.random.randint(10000, size=10)
rand_centroids = None
with open("test_img") as f :
    lines = f.readlines()
    rand_centroids = [lines[index] for index in rand_indices]

with open("part-00000", 'w') as f :
    for centroid in rand_centroids :
        f.write(centroid)

os.system("hadoop fs -mkdir /user/s1155170000/hw3/2c")
os.system("hadoop fs -mkdir /user/s1155170000/hw3/2c/0")
os.system("hadoop fs -put part-00000 /user/s1155170000/hw3/2c/0/")

def check_converge(iter) :
    os.system("hadoop fs -get /user/s1155170000/hw3/2c/" + str(iter))
    cur_centroids = None
    with open(str(iter) + "/part-00000") as f :
        cur_centroids = np.array([list(map(float, vector.split(','))) for vector in f.readlines()])

    os.system("hadoop fs -get /user/s1155170000/hw3/2c/" + str(iter-1))
    prev_centroids = None
    with open(str(iter-1) + "/part-00000") as f :
        prev_centroids = np.array([list(map(float, vector.split(','))) for vector in f.readlines()])

    diff = np.linalg.norm(cur_centroids - prev_centroids)
    print("D(curr,prev) =", diff)
    return diff <= .05

# K-means main loop
iter = 0
while (not check_converge(iter)) if iter > 0 else True :
    if os.system("hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dicvmc2.ie.cuhk.edu.hk/user/s1155170000/hw3/2c/" + str(iter) + 
                 "/part-00000 -file mapper.py -mapper \"python3 mapper.py\" -file reducer.py -reducer \"python3 reducer.py\" -input /user/s1155170000/data/test_img -output /user/s1155170000/hw3/2c/"
                 + str(iter+1)) != 0 :
        print("iteration", iter, "error!")
        exit(1)
    iter += 1

print("iterations required for convergence:", iter)

# Compute Accuracy
final_centroids = None
with open(str(iter) + "/part-00000") as f :
    final_centroids = [np.array(list(map(float, vector.split(',')))) for vector in f.readlines()]
labels = None
with open("test_label") as f :
    labels = [int(line.strip()) for line in f.readlines()]
with open("test_img") as f :
    lines = f.readlines()
    cen_count = [defaultdict(lambda: 0) for _ in range(10)]
    for i in range(10000) :
        point = np.array(list(map(float, lines[i].split(','))))
        dists = [np.linalg.norm(point - centroid) for centroid in final_centroids]
        cen_count[dists.index(min(dists))][labels[i]] += 1
    for i in range(10) :
        count = cen_count[i]
        label = None
        for key in count :
            if count[key] == max(count.values()) :
                label = key
                break
        print("Centroid", i, ":")
        print("Major label of the cluster:", label)
        print("# Train images belonging to the cluster:", sum(count.values()))
        print("# Correctly clustered images:", count[label])
        print("Classification Accuracy:", count[label]/sum(count.values()))
        print()
