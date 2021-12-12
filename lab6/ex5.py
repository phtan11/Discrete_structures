def gcd(a,b):
    if b==0:
        return a
    print("%d" %(a) + "= %d*%d" %(b,a//b) +"+%d"%(a%b))
    return gcd(b,a%b)
print(gcd(662,414))