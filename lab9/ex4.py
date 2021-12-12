A1=([[0,0,2,3,3,0],
            [0,0,3,2,0,0],
            [0,0,0,2,8,6],
            [0,0,0,0,0,5],
            [0,0,0,0,0,3],
            [0,0,0,0,0,0]])
def toLoE(A):
    res = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]!=0:
                res.append([chr(i+65),chr(j+65),A[i][j]])
    return res

print(toLoE(A1))