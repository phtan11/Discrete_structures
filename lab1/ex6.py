def tong(a,b):
    return a+b
def tru(a,b):
    return a-b
def nhan(a,b):
    return a*b
def chia(a,b):
    return a/b
def mu(a,b):
    return a**b
def operation(x):
    switcher=\
    {
        1: tong(a,b),
        2: tru(a,b),
        3: nhan(a,b),
        4: chia(a,b),
        5:  mu(a,b)
    }
    return switcher.get(x,"khong co")
a=3
b=2
print(operation(4))