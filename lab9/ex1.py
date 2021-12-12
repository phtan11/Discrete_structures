

A=[[1,2,3],
    [4,5,6],
    [7,8,9]]
B=[[10,11,12],
    [13,14,15],
    [16,17,18]]
def createMatrix(row,col): #tao 1 matrix rong
    result =[]
    for i in range(row):
        temp =[]
        for j in range(col):
            temp.append(0)
        result.append(temp)
    return result
def mPlus(A,B):
    C=createMatrix(len(A),len(A[0]))
    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        return C
    for i in range(len(A)):
        for j in range(len(B)):
            C[i][j] = A[i][j] + B[i][j]
    return C
def mMinus(A,B):
    C=createMatrix(len(A),len(A[0]))
    if (len(A) != len(B) or len(A[0]) != len(B[0])):
        return C
    for i in range(len(A)):
        for j in range(len(B)):
            C[i][j] = A[i][j] - B[i][j]
    return C
def mMultiply(A,B): #C(i,j) = A(i,k)*B(k,j)
    rowA=len(A)
    colA=len(A[0])
    rowB = len(B)
    colB=len(B[0])
    C = createMatrix(rowA,colB)
    if colA!= rowB:
        return C
    else: #Tổng C = hàng A * với hết cột của B => rồi hàng tiếp theo của A.
        for i in range(rowA):
            for j in range(colB):
                for k in range(colA):
                    C[i][j] += (A[i][k]*B[k][j])
    return C
def mTranspose(A,B):
    TransMatrix = createMatrix(len(A), len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            TransMatrix[j][i] = A[i][j]
    return TransMatrix
print(mPlus(A,B))
print(mMinus(A,B))
print(mMultiply(A,B))
print(mTranspose(A,B))