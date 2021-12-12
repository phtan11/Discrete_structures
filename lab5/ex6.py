A=[[2 ,0 ,5 ,0 ,3 ,0],
[3 ,0 ,0 ,0 ,0 ,0],
[0 ,6 ,2 ,0 ,5 ,0],
[3 ,0 ,9 ,0 ,25 ,0],
[0 ,0 ,2 ,4 ,5 ,0],
[0 ,0 ,0 ,0 ,0 ,5]]
def lImplies(p,q):
    if p:
        return q
    else:
        return True
def isOdd(a):
    if a%2!=0:
        return True
    return False
def isPrime(a):
    if(a<2):
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def isSquare(a):
    return a**2
def isGreater(a,b):
    return True if a>b else False
def isEqual(a,b):
    return True if a==b else False

#a
def cauA(a):
    if (not isOdd(a) and isPrime(a)):
        return True
    return False
def cauB(a):
    if ((lImplies(isOdd(a),isSquare(a))) == False):
        return False
    return True
def cauC(a):
    if ((lImplies(isOdd(a),isGreater(a,2))) == False):
        return False
    return True
def cauD(a):
    if (lImplies(isPrime(a),(isGreater(a,3) or isEqual(a,3)))):
        return True
    return False
check = False
print("cau a:")
for i in range(len(A)):
    for j in range(len(A[0])):
        if cauA(A[i][j]):
            check = True
            break
if check:
    print("True")
else:
    print("False")
check = True
print("cau b:")
for i in range(len(A)):
    for j in range(len(A[0])):
        if cauB(A[i][j])==False:
            check = False
            break
if check:
    print("True")
else:
    print("False")
print("cau c:")
check = True
for i in range(len(A)):
    for j in range(len(A[0])):
        if cauC(A[i][j])==False:
            check= False
            break
if check:
    print("True")
else:
    print("False")
print("cau d:")
check =False
for i in range(len(A)):
    for j in range(len(A[0])):
        if cauA(A[i][j]):
            check =True
            break
if check:
    print("True")
else:
    print("False")
