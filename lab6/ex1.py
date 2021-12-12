def nextPrime(n):
    np =[]
    isPrime=[]
    for i in range(n+1,n+200):
        np.append(i)
    for j in np:
        valIsPrime = True
        for x in range(2,j-1):
            if j%x==0:
                valIsPrime = False
                break
        if valIsPrime:
            isPrime.append(j)
    return min(isPrime)
print(nextPrime(1))