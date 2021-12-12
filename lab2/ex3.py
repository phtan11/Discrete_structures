import itertools
from ex1 import lImplies
#Cach 1
table = list(itertools.product([True, False],repeat =3))
print("expression 1")
for i in table:
    i +=(i[0] and i[1],lImplies(i[0] and i[1],i[2]))
    print(i)
print("expression 2")
for i in table:
    i +=(i[0] and i[1],lImplies(i[2],i[0] and i[1]))
    print(i)

#cach 2: ap dung ex2 roi ep vao bang


