from ex1 import lImplies
from ex1 import lAnd
from ex1 import lOr
from ex1 import lXor
from ex1 import lNot
from ex1 import lEquivalent
P=[True, True, False, False]
Q =[True,False, True, False]
#a
def iLImplies(P,Q):
    R=[]
    for p,q in zip(P,Q):
        R.append(lImplies(p,q))
    return R
print(iLImplies(P,Q))

#b
def lLAnd(P,Q):
    R=[]
    for p,q in zip(P,Q):
        R.append(lAnd(p,q))
    return R
print(lLAnd(P,Q))
#c
def iLOr(P,Q):
    R =[]
    for p,q in zip(P,Q):
        R.append(lOr(p,q))
    return R
print(iLOr(P,Q))
#d
def lLXor(P,Q):
    R=[]
    for p,q in zip(P,Q):
        R.append(lXor(p,q))
    return R
print(lLXor(P,Q))
#e
def lLNot(P):
    R=[]
    for p in P:
        R.append(lNot(p))
    return R
print(lLNot(P))
#f
def lLEquivalent(P,Q):
    R=[]
    for p,q in zip(P,Q):
        R.append(lEquivalent(p,q))
    return R
print(lLEquivalent(P,Q))