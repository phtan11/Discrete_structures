from ex1 import lImplies
from ex1 import lNot
import itertools
table = list(itertools.product([True,False], repeat = 5))
def A(table):
    check = False
    dem  = 0
    for i in table:
        premise1 = lImplies(i[0],i[2])
        premise2 = lImplies(lNot(i[0]),i[1])
        premise3 = lImplies(i[1],i[3])
        premise4 = lImplies(lNot(i[2]),i[3])
        if(premise1 == premise2 == premise3 == True):
            check = True
            if(premise4 != True):
                dem =1
    if(check):
        if(dem ==0):
            return True
    if(check == False):
        return False
print("Cau a:")
if(A(table)):
    print("Valid")
else:
    print("Invalid")

def cC(table):
    check = False
    dem  = 0
    for i in table:
        pre1 = lImplies(i[0],i[1])
        pre2 = lNot(i[2]) or i[3]
        pre3 = i[0] or i[2]
        pre4 = lImplies(lNot(i[1]),i[3])
        if(pre1 == pre2 == pre3 == True):
            check = True
            if(pre4 != True):
                dem =1
    if(check):
        if(dem ==0):
            return True
    if(check == False):
        return False
print("Cau C:")
if(cC(table)):
    print("Valid")
else:
    print("Invalid")

def cB(table):
    check = False
    dem  = 0
    for i in table:
        pre1 = lImplies(i[0],lImplies(i[1],i[2]))
        pre2 = i[0] or i[3]
        pre3 = lImplies(i[4],i[1])
        pre4 = lImplies(lNot(i[2]),lNot(i[4]))
        if(pre1 == pre2 == pre3 == True):
            check = True
            if(pre4 != True):
                dem =1
    if(check):
        if(dem ==0):
            return True
    if(check == False):
        return False
print("Cau B:")
if(cB(table)):
    print("Valid")
else:
    print("Invalid")

def cD(table):
    check = False
    dem  = 0
    for i in table:
        pre1 = i[0]
        pre2 = lImplies(i[0], i[2])
        pre3 = lImplies(i[0],lImplies(i[1],lNot(i[2])))
        pre4 = i[3]
        if(pre1 == pre2 == pre3 == True):
            check = True
            if(pre4 != True):
                dem =1
    if(check):
        if(dem ==0):
            return True
    if(check == False):
        return False
print("Cau D:")
if(cD(table)):
    print("Valid")
else:
    print("Invalid")