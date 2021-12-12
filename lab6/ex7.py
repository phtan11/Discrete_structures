def dec2Bin(n):
    if(n==0):
       return 0
    print("%d=" %(n) +"2*%d"%(n//2) + "+%d" %(n%2))
    return  (n%2+10*dec2Bin(n//2))
print(dec2Bin(6))
