def sumN(n):
    sum =0
    if(n>0):
        for i in range (1,n+1):
            sum+=i
    else:
        for i in range(0,n-1,-1):
            sum +=i
    return sum
z= sumN(-4)
print(z)    