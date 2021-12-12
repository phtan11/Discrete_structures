import itertools
table = list(itertools.product([True,False], repeat = 4))
#print(table)
def lImplies(p,q):
    if p:
        return q
    else:
        return True
#a
for i in range(len(table)):
    p = table[i][0]
    q = table[i][1]
    r = table[i][2]
    t = table[i][3]

    S1 = lImplies(q,t)
    S2 = lImplies(p,t)
    S3 = lImplies(r,t)

    table[i] += (S1,S2,S3)
    print(table[i])

countcr = 0
countvalid = 0
for i in range(len(table)):
    p = table[i][0]
    S1 = table[i][4]
    S2 = table[i][5]
    S3 = table[i][6]
    t = table[i][3]
    if p==S1==S2==S3== True:
        countcr+=1
        if t== True:
            countvalid +=1
print("cau a:")
if countcr==countvalid:
    print("valid,prove")
elif countcr>countvalid:
    print("invalid")
if countvalid==0 and countcr>0:
    print("disprove")

for i in range(len(table)):
    p= table[i][0]
    q= table[i][1]
    r= table[i][2]
    s= table[i][3]
    v= table[i][4]

    S1=lImplies(r,not q)
    S2=lImplies(p,v)
    S3=lImplies(s,r)
    S4=lImplies(not s,not v)
    table[i] += (S1,S2,S3,S4)
    print(table[i])
countcr= 0
countvalid= 0
for i in range(len(table)):
    p= table[i][0]
    S1= table[i][5]
    S2= table[i][6]
    S3= table[i][7]
    S4= table[i][8]
    v= table[i][4]
    if S1==S2==S3==S4==True:
        countcr += 1
        if v==True:
            countvalid += 1
print("cau b:")
if countcr==countvalid:
    print("prove")
elif countcr>countvalid:
    print("invalid")
if countcr>0 and countvalid==0:
    print("disprove")