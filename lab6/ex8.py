#import math
# def bin2Dec(n,i):
#     if(n==0):
#         return 0
#     return (int)(n%10)*math.pow(2,i)+bin2Dec(n//10,i+1)
# print(bin2Dec(110,0))

def dec2Bin(n):
    if(n==0):
       return 0
    print("%d=" %(n) +"2*%d"%(n//2) + "+%d" %(n%2))
    return  (n%2+10*dec2Bin(n//2))
print(dec2Bin(5.5))