#a
def lImplies(p,q):
    if p:
        return q
    else:
        return True
print(lImplies(True,True))

#b
def lAnd(p,q):
    if p:
        return q;
    else:
        return False
print(lAnd(True,False))

#c
def lOr(p,q):
    if p:
        return True
    else:
        return q
print(lOr(False,False))

#d Xor: 2 cai deu true hoac false thi la false. 2 dua khac nhau la true
def lXor(p,q): 
    return p != q
print(lXor(True,True))
#e
def lNot(p):
    return not p
print(lNot(True))
#f deu ca 2 deu cung true va cung false thi true. nguoc lai false
def lEquivalent(a,b):
    if a and b:
        return True
    elif not a and not b:
        return True
    else:
        return False

print(lEquivalent(False,False))

