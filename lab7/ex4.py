def Fac(n):
    if(n==0):
        return 1
    return n*Fac(n-1)
def wayToChooseP(n,k):
    if k == 0 or k==n:
        return 1
    return Fac(n)
print(wayToChooseP(50,1))