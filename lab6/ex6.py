def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    #c1
    # greater = a if (a>b) else b 
    # lcm=0
    # while True:
    #     if((greater%a==0) and (greater %b==0)):
    #         lcm=greater
    #         break
    #     greater += 1
    # return lcm
    #c2
    return (a*b)//gcd(a,b)

print(gcd(54,24))
print(lcm(54,24))
# print(lcm(54,24)*gcd(54,24))