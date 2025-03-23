#!/usr/bin/env python
import sys

referee_set = {}

for line in sys.stdin:
    line = line.strip().split()
    referrer = int(line[0])
    referee_list = map(int, line[1:])
    referee_set[referrer] = set(referee_list)

def similarity(A, B):
    return float(len(A.intersection(B))) / float(len(A.union(B)))

for referrer1 in referee_set.keys():
    for referrer2 in referee_set.keys():
        if referrer1 == referrer2 : continue
        set1 = referee_set[referrer1]
        set2 = referee_set[referrer2]
        common_referees = list(set1.intersection(set2))
        simscore = similarity(set1, set2)

        if simscore > 0 :
            print("{web1}:{web2}, {{ {web_list} }}, {score}".format(
                web1=referrer1,
                web2=referrer2,
                web_list=','.join(map(str, common_referees)),
                score=simscore
            ))
