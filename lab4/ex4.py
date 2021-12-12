def A():
    tongVt =0
    tongVp =0
    for x in range(0,11):
        for y in range(0,11):
            tongVt += (x+y)**2
            tongVp += (x+2*y)**2
    if(tongVt > tongVp):
        print("prove")
    else:
        print("Disprove")
    tongVt =0
def GT(n):
    if n==0:
        return 1
    return n*GT(n-1)

def B():
    tong=0
    for x in range(0,11):
        tong += GT(x)
    if(GT(20) < tong):
        print("prove")
    else:
        print("Disprove")

def C():
    tong=0
    for x in range(0,11):
        tong += 3*(x**2)
    if(10*10*10 <= tong):
        print("prove")
    else:
        print("Disprove")

def D():
    tong=0
    for x in range(5,11):
        tong += (4*x*x*x + 6*x*x + 2*x)
    if(tong > (10*10*10*10 + 2*10*10*10 + 10*10 - 5*5*5*5 -2*5*5*5 -5*5)):
        print("prove")
    else:
        print("Disprove")
A()
B()
C()
D()