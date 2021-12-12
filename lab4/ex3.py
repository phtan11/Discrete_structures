
#a
def A():
    check = False
    for i in range(100):   
        if(i*i*i < i):
            check = True
            break
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect")
def checkIsNotPrime(n):
    if(n<2):
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return True
                break
    return False
def B():
    check = False
    for i in range(0,100):   
        if(i%2!=0):
            if(checkIsNotPrime(i*3+1)):
                check = True
                break
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect")

def C():
    check = False
    for i in range(1,100):   
        if(i%2!=0):
            if(checkIsNotPrime(i*5+3)):
                check = True
                break
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect")

def F(): #dung het thi moi dung
    check = True
    for c in range(0,101):
        if(c**2 < c):
            check = False
            break
    if(check):
        print("the given statement is correct when x equal to %d" %(c))
    else:
        print("the given statement is incorrect")

def D():
    check = True
    for c in range(0,101): #ton tai it nhat 1 phan tu
        if(c % 4 !=0):
            for a in range(0,101): # voi moi a b 
                for b in range(0,101):
                    if(c**2 == (a**2 + b**2)):
                        check = False
                        break
    if(check):
        print("the given statement is correct when x equal to %d" %(c))
    else:
        print("the given statement is incorrect")

def E():
    check = True
    for c in range(0,101): #ton tai it nhat 1 phan tu
        if(c % 5 !=0):
            for a in range(0,101): # voi moi a b 
                for b in range(0,101):
                    if(c**2 == (a**2 + b**2)):
                        check = False
                        break
    if(check):
        print("the given statement is correct when x equal to %d" %(c))
    else:
        print("the given statement is incorrect")                 
A()
B()
C()
F()
D()
E()