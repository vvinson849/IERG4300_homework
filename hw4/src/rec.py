import numpy as np

utilities = np.array([[2, 1, 5, 4, 3, 0],
                      [0, 2, 0, 3, 5, 4],
                      [5, 0, 4, 1, 4, 2],
                      [2, 3, 4, 5, 0, 0],
                      [0, 4, 1, 0, 3, 2]])

user4 = utilities[3]
top_neighbours = []
for i in range(len(utilities)) :
    useri = utilities[i]
    if useri[4] > 0 :
        top_neighbours.append((i, np.corrcoef(user4, useri)[0,1]))
top_neighbours = sorted(top_neighbours, key=lambda x: x[1], reverse=True)[:2]
pred_r = sum([nei[1]*utilities[nei[0]][4] for nei in top_neighbours]) / sum([nei[1] for nei in top_neighbours])
print("Predicted Rating of User-User CF =", pred_r)

bookE = utilities.T[4]
top_neighbours = []
for i in range(len(utilities.T)) :
    booki = utilities.T[i]
    if user4[i] > 0 and i != 4 :
        top_neighbours.append((i, np.corrcoef(bookE, booki)[0,1]))
top_neighbours = sorted(top_neighbours, key=lambda x: x[1], reverse=True)[:2]
pred_r = sum([nei[1]*user4[nei[0]] for nei in top_neighbours]) / sum([nei[1] for nei in top_neighbours])
print("Predicted Rating of Item-Item CF =", pred_r)
