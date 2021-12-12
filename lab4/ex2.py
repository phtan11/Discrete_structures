import math
def A():
    check=True
    for i in range(0,100):
        if(i**2 == 15*15 + 16*16):
            break
        else:
            check = False
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect for all values x within the given domain.")
        
def B():
    b = 12*12 + 16*16
    check=False
    for i in range(0,100):
        if i**2 == b:
            check = True
            break
        else:
            check = False
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect for all values x within the given domain.")
def C():
    check=True
    for i in range(-50,50):
        if(i**2 >= 99*i):
            break
        else:
            check = False
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect for all values x within the given domain.")
def D():
    check=True
    for i in range(50,100):
        if((i*(i+1)*(i+2))%6 != 0):
            break
        else:
            check = False
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect for all values x within the given domain.")
def E():
    check=False
    for i in range(100):
        for j in range(100):
            if(math.sqrt(i+j) == (math.sqrt(i) + math.sqrt(j))):
                check=True
                break
            else:
                continue
            break
    if(check):
        print("the given statement is correct when x equal to %d" %(i))
    else:
        print("the given statement is incorrect for all values x within the given domain.")


print("Cau a:")
A()
print("Cau b:")
B()
print("Cau c:")
C()
print("Cau d:")
D()
print("Cau e:")
E()
