import math
def bin2Dec(n,i):
    if(n==0):
        return 0
    return (n%10)*math.pow(2,i)+bin2Dec(n//10,i+1)
def convertBase(a,base1,base2):
    dec=int(bin2Dec(a,0))
    return oct(dec)
print(convertBase(111,10,16))