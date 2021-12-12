#a

A=[None,2,
7,5,
2,6,None,9,
None,None,5,11,None,None,4,None]
#qui luat xuong dong.
# 1 3 7 15
print("cau a:")
n=1
for i in range(1,len(A)):
    print(A[i], end=' ')
    if i ==2**n - 1:
        print()
        n+=1


# #b

B=[None,50,
17,76,
9,23,54,None,
None,14,19,None,None,72,None,None,
None,None,12,None,None,None,None,None,67,None,None,None,None,None]
print("cau b:")
n=1
for i in range(1,len(B)):
    print(B[i], end=' ')
    if i ==2**n - 1:
        print()
        n+=1
