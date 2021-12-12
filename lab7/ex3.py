def wayToChoose(n,k):
    if k==0 or k==n:
        return 1
    return wayToChoose(n-1,k) + wayToChoose(n-1,k-1)
def check():
    n=50
    k=0
    while wayToChoose(n,k) <1000:
        k+=1
    if(1000-wayToChoose(n,k-1) < wayToChoose(n,k) - 1000):
        return k-1
    else:
        return k
print(check())
print(wayToChoose(50,1))
print(wayToChoose(50,2))
print(wayToChoose(50,3))



