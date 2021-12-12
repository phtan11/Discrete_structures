a="For all people, if they are blond then they are westerners."
b="Exist a person, whose hair is black but is a westerner."
c ="For all students, if they study correctly then they have high score."
d = "For every mammal, if they live in the sea, they are either dolphins or whales."
e="For every bird, if they don’t have wings and can swim then they are penguins."
f="Exist a bird, who have wing but can’t fly."

def formalConvert(S):
    P =""
    F=""
    D=""
    Q=""
    #F
    if S.startswith("For all"):
        F = "For all x,P(x) -> Q(x)"
    elif S.startswith("Exist"):
        F = "Exist x such that P(x) ^ Q(x)"
    elif S.startswith("For every"):
        F= "For all x,P(x) -> Q(x)"
    #D
    arr = S.split(',')
    if arr[0].find("For all") > -1:
        D = arr[0].replace("For all ", '')
    elif arr[0].find("Exist") > -1:
        D = arr[0].replace("Exist ", '')
    elif arr[0].find("For every")>-1:
        D = arr[0].replace("For every ", '')
    #P
    #if then
    arr1 = arr[1].split()
    i=-1
    for a in range(len(arr1)):
        if arr1[a] == "then":
            i = a
            break
    
    if arr[1].find("then") > -1 and arr[1].startswith(" if"):
        P =" ".join(arr[1].split()[2:i])
        Q =" ".join(arr[1].split()[i+3:])
    #P
    #For every
    if len(arr) == 3:
        P = " ".join(arr[1].split()[2:])
        Q = " ".join(arr[2].split()[2:])

    #P
    #Exist
    #tim chu 'but'
    j=-1
    arr3 = arr[1].split()
    for a in range(len(arr3)):
        if arr3[a] == "but":
            j=a
            break
    if arr[0].startswith("Exist"):
        if arr[1].startswith(" whose"):
            P =" ".join(arr[1].split()[2:j])
            Q = " ".join(arr[1].split()[j+3:])
        if arr[1].startswith(" who"):
            P = " ".join(arr[1].split()[1:j])
            Q =" ".join(arr[1].split()[j+1:])
    return [D,P,Q,F]
print(formalConvert(a))
print(formalConvert(b))
print(formalConvert(c))
print(formalConvert(d))
print(formalConvert(e))
print(formalConvert(f))