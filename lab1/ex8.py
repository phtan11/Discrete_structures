A = [[3, 2, 6],
     [5, 1, 6],
     [7, 8, 9]]

B = [[7, 8, 4],
     [4, 8, 3],
     [1, 1, 0]]

C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k]*B[k][i]
for z in C:
    print(z)
