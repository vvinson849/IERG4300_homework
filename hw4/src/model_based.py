import numpy

numpy.random.seed(1155176920)

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.001:
            break
    return P, Q.T

R = numpy.array([[2, 1, 5, 4, 3, 0],
                 [0, 2, 0, 3, 5, 4],
                 [5, 0, 4, 1, 4, 2],
                 [2, 3, 4, 5, 0, 0],
                 [0, 4, 1, 0, 3, 2]])

N = len(R)
M = len(R[0])
K = 3

P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = numpy.dot(nP, nQ.T)
print("Original model-based CF:")
print(nR)

print()

def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i, :], Q[:, j])
                    P_update = alpha * (2 * eij * Q[:, j] - beta * P[i, :])
                    Q_update = alpha * (2 * eij * P[i, :] - beta * Q[:, j])
                    P[i, :] += P_update
                    Q[:, j] += Q_update
        eR = numpy.dot(P, Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i, :], Q[:, j]), 2)
                    for k in range(K):
                        e = e + (beta / 2) * (pow(P[i][k], 2) + pow(Q[k][j], 2))
        if e < 0.001:
            break
    return P, Q.T

R = numpy.array([[2, 1, 5, 4, 3, 0],
                 [0, 2, 0, 3, 5, 4],
                 [5, 0, 4, 1, 4, 2],
                 [2, 3, 4, 5, 0, 0],
                 [0, 4, 1, 0, 3, 2]])

N = len(R)
M = len(R[0])
K = 3

P = numpy.random.rand(N, K)
Q = numpy.random.rand(M, K)

nP, nQ = matrix_factorization(R, P, Q, K)
nR = numpy.dot(nP, nQ.T)
print("Corrected model-based CF:")
print(nR)
