import itertools
#C1
def listAlphabet():
    return [chr(i) for i in range(ord('A'),ord('Z')+1)]
def Not(p):
    return not p
def OR(p,q):
    if p:
        return True
    else:
        return q
def AND(p,q):
    if p:
        return q
    else:
        return False
def Implies(p,q):
    if not(p) == True:
        return True
    else:
        return q
def BiImplies(p,q):
    if (p== True and q == True) or (p== False and q== False):
        return True
    else:
        return False
def compare(a):
    if a=="~":
        return 6
    if a=="&":
        return 5
    if a=="|":
        return 4
    if a==">":
        return 3
    if a=="=":
        return 2
    if a=="(":
        return 1
def Infix2Postfix(Infix):
    Postfix = ""
    logic1 = ["&", "|" , "~" ,  "(","=", ">"]
    operators =[]
    stack = []
    count=0
    for i in range(0,len(Infix)):
        if Infix[i] in listAlphabet():
            stack.append(Infix[i])
            # if len(operators) > 0 and operators[len(operators)-1] =='~':
            #     stack.append(operators.pop())
        elif Infix[i] in logic1: #["&", "|" , "~" ,  "(","=", ">"]
            if len(operators)==0:
                operators.append(Infix[i])
            else:
                if Infix[i] =="(":
                    operators.append(Infix[i])
                else:
                    if compare(operators[len(operators)-1])  > compare(Infix[i]): 
                        stack.append(operators.pop())
                        if(len(operators)>0):
                            stack.append(operators.pop())
                        operators.append(Infix[i])
                    else:
                        operators.append(Infix[i])
        elif Infix[i] ==")":
            c = 0
            if Infix[i-1] == ")":
                continue
            while len(operators) >0:
                stack.append(operators.pop())
                if (len(operators) >0 and operators[len(operators)-1] =="("):
                    operators.pop()
                    c+=1
                    if c ==2:
                        break
    while len(operators) +1> 1:
        stack.append(operators.pop())
    for i in stack:
        Postfix += i
    return Postfix

def Postfix2Truthtable(Postfix):
    stack = []
    for i in Postfix:
        if i in listAlphabet():
            if not(i in stack):
                stack.append(i)
    amountOfRow = len(stack)
    table = list(itertools.product([False,True], repeat = amountOfRow))
    stack.sort()
    stack1=[]
    Truthtable =[]
    for i in table:
        data=[]
        for k in i:
            data.append(k)
            print(data)
        for j in Postfix: #RPQ&|
            if j in listAlphabet():
                stack1.append(data[stack.index(j)])
            elif j=="~":
                a= stack1.pop()
                data.append(Not(a))
                stack1.append(Not(a))
            else:
                a = stack1.pop()
                b = stack1.pop()
                if j =="&":
                    data.append(AND(a,b))
                    stack1.append(AND(a,b))
                elif j == "|":
                    data.append(OR(a,b))
                    stack1.append(OR(a,b))
                elif j == ">":
                    data.append(Implies(b,a))
                    stack1.append(Implies(b,a))
                elif j =="=":
                    data.append(BiImplies(a,b))
                    stack1.append(BiImplies(a,b))
        Truthtable.append(data)
        data=[]
    return Truthtable

# print(Infix2Postfix("R|(P&Q)"))
print(Infix2Postfix("~P|(Q&R)>R"))
# print(Infix2Postfix("P|(R&Q)"))
# print(Infix2Postfix("(P>Q)&(Q>R)"))
# print(Infix2Postfix("(P|~Q)>~P=(P|(~Q))>~P"))
print()

# s =Infix2Postfix("R|(P&Q)")
# print(Postfix2Truthtable(s))

q=Infix2Postfix("~P|(Q&R)>R")
print(Postfix2Truthtable(q))

# w =Infix2Postfix("P|(R&Q)")
# print(Postfix2Truthtable(w))

# e =Infix2Postfix("(P>Q)&(Q>R)")
# print(Postfix2Truthtable(e))

# z =Infix2Postfix("(P|~Q)>~P=(P|(~Q))>~P")
# print(Postfix2Truthtable(z))