import itertools
from ex1 import lImplies
from ex1 import lNot
from ex1 import lEquivalent
#1
table=list(itertools.product([True,False], repeat = 8))
print("expression 1:\n")
for i in table:
    i += (i[0] or i[1],i[0] and i[1],lNot(i[0]) or lNot(i[1]),lImplies(i[0] or i[1],i[0] and i[1]),lImplies(lImplies(i[0] or i[1],i[0] and i[1]),lNot(i[0]) or lNot(i[1])))
    print(i)

#2
print("expression 2:\n")
for i in table:
    i += (lNot(i[0]),i[1] and i[2],(lNot(i[0]) or (i[1] and i[2])),lImplies((lNot(i[0]) or (i[1] and i[2])),i[2]))
    print(i)
#3
print("expression 3:\n")
for i in table:
    i += (lImplies(i[0],i[1]),lImplies(i[1],i[2]),(lImplies(i[0],i[1]) and lImplies(i[1],i[2])))
    print(i)
#4
print("expression 4:\n")
for i in table:
    i += ((i[0] or (i[1] and i[2])),((i[0] or i[1]) and (i[0] or i[2])),lEquivalent((i[0] or (i[1] and i[2])),((i[0] or i[1]) and (i[0] or i[2]))) )
    print(i)
#5
print("expression 5:\n")
for i in table:
    i += (i[0] or i[1],lNot(i[2]) or i[3],lImplies(i[0] or i[1],lNot(i[2]) or i[3]))
    print(i)
#6
print("expression 6:\n")
for i in table:
    i += (i[0] or i[3],lImplies(i[2],i[3]),lImplies(i[0] or i[3],i[1]),lImplies(lImplies(i[0] or i[3],i[1]),lImplies(i[2],i[3])))
    print(i)
#7
print("expression 7:\n")
for i in table:
    i += (i[0] or (i[1] and i[2]),i[0] and i[1], i[0] or i[2],i[3] or lNot(i[3]),(((i[0] or i[1]) and (i[0] or i[2])) and (i[3] or lNot(i[3]))),lEquivalent(i[0] or (i[1] and i[2]), (((i[0] or i[1]) and (i[0] or i[2])) and (i[3] or lNot(i[3])))))
    print(i)
 