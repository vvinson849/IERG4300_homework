#!/usr/bin/env python3
import os
import numpy as np

np.random.seed(4300)

rand_indices = np.random.randint(60000, size=10)
rand_centroids = None
with open("train_img") as f :
    lines = f.readlines()
    rand_centroids = [lines[index] for index in rand_indices]

with open("part-00000", 'w') as f :
    for centroid in rand_centroids :
        f.write(centroid)

os.system("hadoop fs -mkdir /user/s1155170000/hw3/2a")
os.system("hadoop fs -mkdir /user/s1155170000/hw3/2a/0")
os.system("hadoop fs -put part-00000 /user/s1155170000/hw3/2a/0/")

def check_converge(iter) :
    os.system("hadoop fs -get /user/s1155170000/hw3/2a/" + str(iter))
    cur_centroids = None
    with open(str(iter) + "/part-00000") as f :
        cur_centroids = np.array([list(map(float, vector.split(','))) for vector in f.readlines()])

    os.system("hadoop fs -get /user/s1155170000/hw3/2a/" + str(iter-1))
    prev_centroids = None
    with open(str(iter-1) + "/part-00000") as f :
        prev_centroids = np.array([list(map(float, vector.split(','))) for vector in f.readlines()])

    diff = np.linalg.norm(cur_centroids - prev_centroids)
    print("D(curr,prev) =", diff)
    return diff <= .05

iter = 0
while (not check_converge(iter)) if iter > 0 else True :
    if os.system("hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files hdfs://dicvmc2.ie.cuhk.edu.hk/user/s1155170000/hw3/2a/" + str(iter) + 
                 "/part-00000 -file mapper.py -mapper \"python3 mapper.py\" -file reducer.py -reducer \"python3 reducer.py\" -input /user/s1155170000/data/train_img -output /user/s1155170000/hw3/2a/"
                 + str(iter+1)) != 0 :
        print("iteration", iter, "error!")
        exit(1)
    iter += 1

print("iterations required for convergence:", iter)

#os.system("hadoop fs -get /user/s1155170000/hw3/2a/" + str(iter))
final_centroids = None
with open(str(iter) + "/part-00000") as f :
    final_centroids = [np.array(list(map(float, vector.split(',')))) for vector in f.readlines()]
with open("train_img") as f :
    cen_count = [0] * 10
    for line in f.readlines() :
        point = np.array(list(map(float, line.split(','))))
        dists = [np.linalg.norm(point - centroid) for centroid in final_centroids]
        cen_count[dists.index(min(dists))] += 1
    for i in range(10) :
        print("Centroid", i, ":", cen_count[i], ",", ','.join(map(str, final_centroids[i])))
