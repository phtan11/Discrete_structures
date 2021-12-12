import itertools
def readInfix(filename):
    with open(filename) as f:
        Infix = f.readlines()
    return Infix[0]
##########################################Student do these 2 function
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
        elif Infix[i] in logic1:
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
    while len(operators) > 0:
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
##########################################End student part
def writeTruthtable(table):
    import sys
    outfile=sys.argv[0]
    outfile=outfile[0:-2]
    outfile+="txt"
    with open(outfile, 'w') as f:
        for lines in table:
            for item in lines:
                f.write("%s\t" % item)
            f.write("\n")
    f.close()
def main():
    Infix=readInfix("logicexpression.txt")
    Postfix=Infix2Postfix(Infix)
    Truthtable=Postfix2Truthtable(Postfix)
    writeTruthtable(Truthtable)
main()