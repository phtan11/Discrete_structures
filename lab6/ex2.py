def primeFact(p):
    listOfFact =[]
    i =2
    while(p>1):
        if p%i==0:
            listOfFact.append(i)
            p/=i
            i=i-1
        i+=1
    return listOfFact
print(primeFact(60))
def countFact(a):
    t =a[0]
    arr=[]
    s = 0
    for i in range(len(a)):
        if a[i] ==t:
            s += 1
        else:
            t=a[i]
            arr.append(s)
            s=1
    arr.append(s)
    return arr
print(countFact(primeFact(60)))