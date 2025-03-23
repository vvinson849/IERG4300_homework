import numpy as np

# 1a
matrix = np.array([[4, 3, 5, 4, 3, 5],
                   [5, 4, 3, 1, 4, 2],
                   [3, 1, 5, 5, 1, 5],
                   [3, 4, 1, 3, 4, 3],
                   [4, 3, 4, 5, 2, 5]])

U, S, Vh = np.linalg.svd(matrix)
print("U =\n", U)
print()
print("S =\n", S)
print()
print("Vh =\n", Vh)

print()
print()

U_re = U.T[:2].T
S_re = S[:2]
Vh_re = Vh[:2]
print("U_re =\n", U_re)
print()
print("S_re =\n", S_re)
print()
print("Vh_re =\n", Vh_re)

print()
print()

# 1b1
new_person = np.array([5, 3, 4, 3, 5, 1])
new_person_perform = new_person.dot(Vh_re.T)
print("New person's performance =\n", new_person_perform)

print()
print()

# 1b2
def cossim(vec1, vec2) :
    return vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

A_ori = np.array(matrix[0])
C_ori = np.array(matrix[2])
A_con = A_ori.dot(Vh_re.T)
C_con = C_ori.dot(Vh_re.T)
print("Similarity in original space:", cossim(A_ori, C_ori))
print("Similarity in concept space:", cossim(A_con, C_con))

