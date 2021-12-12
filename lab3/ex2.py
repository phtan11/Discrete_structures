a = "For all fish,they need water to survive"
b = "Exist a person,who is left handed"
c = "Exist an employee in the company,who is late to work everyday."
d = "For all fish in this pond,they are Koi fish."
e = "There is at least one creature in the ocean,it can live on land"
def formalConvert(S):
    if S.startswith("For all"):
        F = "Formal form: For all x in D,P(x)"
    elif S.startswith("Exist"):
        F = "Formal form: Exist x in D,P(x)"
    else:
        F ="There is at least D,P(x)"
    
    array = S.split(',')
    if array[0].find("For all ") > -1:
        D = array[0].replace("For all " , '')
    elif array[0].find("Exist ") >-1 :
        D = array[0].replace("Exist " , '')
    elif array[0].find("There is at least ") > -1:
        D = array[0].replace("There is at least " , '')

    if array[1].startswith("who is"):
        P = " ".join(array[1].split()[2:])
    else:
        P = " ".join(array[1].split()[1:])
    return [D,P,F]


print(formalConvert(a))
print(formalConvert(b))
print(formalConvert(c))
print(formalConvert(d))
print(formalConvert(e))