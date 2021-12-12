from ex1 import lNot
from ex1 import lImplies
import itertools
p=[True,False]
def notF(p):
    for i in p:
        if(i == lNot(lNot(i))):
            return True
        else:
            return False
print("C1:")
if(notF(p)):
    print("equivalent")
else:
    print("InEquivalent")


table = list(itertools.product([True,False], repeat = 3))

def C2(table):
    check =0
    for i in table:
        if((lNot(lNot(i[1]) and i[0]) and (i[1] or i[0])) != i[1]):
            check =1
    if(check==0):
        return True
    else:
        return False
print("C2:")
if(C2(table)):
    print("equivalent")
else:
    print("InEquivalent")


def C3(table):
    check = 0
    for i in table:
        if(lNot(i[0] or i[1]) != (lNot(i[0]) or lNot(i[1]))):
            check = 1
    if(check==0):
        return True
    else:
        return False
print("C3:")
if(C3(table)):
    print("equivalent")
else:
    print("InEquivalent")

def C4(table):
    check =0
    for i in table:
        if(lImplies(i[0] or i[1],i[2]) != (lImplies(i[0],i[2]) and lImplies(i[1],i[2]))):
            check =1
    if(check==0):
        return True
    else:
        return False
print("C4:")
if(C4(table)):
    print("equivalent")
else:
    print("InEquivalent")

def C5(table):
    check=0
    for i in table:
        if(lNot(i[0] and i[1]) != (lNot(i[0]) and lNot(i[1]))):
            check=1
    if(check==0):
        return True
    else:
        return False
print("C5:")
if(C5(table)):
    print("equivalent")
else:
    print("InEquivalent")

def C6(table):
    check =0
    for i in table:
        if(lImplies((i[0] or lNot(i[1])) , lNot(i[0])) != lImplies((i[0] or lNot(i[1])),lNot(i[0]))):
            check = 1
    if check == 0:
        return True
    else:
        return False
print("C6:")
if(C6(table)):
    print("equivalent")
else:
    print("InEquivalent")


def C7(table):
    check =0
    for i in table:
        if(lNot(i[0] or i[1]) != (lNot(i[0]) and lNot(i[1]))):
            check = 1
    if check == 0:
        return True
    else:
        return False
print("C7:")
if(C7(table)):
    print("equivalent")
else:
    print("InEquivalent")

