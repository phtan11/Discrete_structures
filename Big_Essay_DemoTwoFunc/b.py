import itertools
def lAnd(p,q):
    return p and q

def lOr(p,q):
    return p or q

def lNot(p):
    return not p

def lImplies(p,q):
    if p:
        return q
    else:
        return True

def lBiImplies(p,q):
    return p == q

def Infix2Postfix(Infix):
    tempstr = ""
    operration = []
    curr = -1

    for i in range(0,len(Infix)):
        if (Infix[i].isalpha()):
            tempstr = tempstr + Infix[i]
            if len(operration) > 0 and operration[len(operration)-1] == '~':
                tempstr = tempstr + operration[curr]
                del operration[len(operration)-1]
           
        else: 
            if (Infix[i] == '~' or Infix[i] == '&' or Infix[i] == '|' or Infix[i] == '('):
                operration.append(Infix[i])
           
                
            else: #dau ) or > or =
                if (Infix[i] == ')'): #push util it = (
                     
                    while (operration[len(operration)-1] != '('):
                        tempstr = tempstr + operration[len(operration)-1]
                        del operration[len(operration)-1]
                    del operration[len(operration)-1]
                else: #> or =
                    while (len(operration) > 0 and (operration[len(operration)-1] != '=' and operration[len(operration)-1] != '>' and operration[len(operration)-1] != '(')):
                        tempstr = tempstr + operration[len(operration)-1]
                        del operration[len(operration)-1]
                   
                    operration.append(Infix[i]) 
    while (len(operration) > 0):
        tempstr = tempstr + operration[len(operration)-1]
        del operration[len(operration)-1]
    Postfix=tempstr  
    return Postfix
def Postfix2Truthtable(Postfix):
    char_num = 0
    alpha_arr = {"":""}
    Postfix = Postfix.upper()
    postfix_stack = []
    #dem so cot can them vao
    for i in range(0, len(Postfix)):
        postfix_stack.append(Postfix[i])
        if Postfix[i].isalpha():
            alpha_arr[Postfix[i]] = 1
     

    index = 0
    char_num = 0
    address_table_arr = {}
    for k in range(ord('A'),ord('Z')+1):
        if chr(k) in alpha_arr: 
            address_table_arr[chr(k)] = index
            index += 1
            char_num += 1

    print(char_num)
    print(address_table_arr)
    table = list(itertools.product([True, False], repeat = char_num))
    #xu ly stack
    
    
    k = 0
    while k < len(postfix_stack):
        if (not postfix_stack[k].isalpha()) and (len(postfix_stack[k])==1 and (not postfix_stack[k] in address_table_arr)):
            for i in range(len(table)):
                if (postfix_stack[k] == '&'):
                    table[i] += (lAnd(table[i][address_table_arr[postfix_stack[k-2]]], table[i][address_table_arr[postfix_stack[k-1]]])),
                else:
                    if postfix_stack[k] == '|': 
                        table[i] += (lOr(table[i][address_table_arr[postfix_stack[k-2]]], table[i][address_table_arr[postfix_stack[k-1]]])),
                    else: 
                        if postfix_stack[k] == '>': 
                            table[i] += (lImplies(table[i][address_table_arr[postfix_stack[k-2]]], table[i][address_table_arr[postfix_stack[k-1]]])),
                        else:                    
                            if postfix_stack[k] == '=': 
                                table[i] += (lBiImplies(table[i][address_table_arr[postfix_stack[k-2]]], table[i][address_table_arr[postfix_stack[k-1]]])),
                            else: #'~'
                                table[i] += (lNot(table[i][address_table_arr[postfix_stack[k-1]]])),

                
            if postfix_stack[k] == '~':
                postfix_stack[k-1] = postfix_stack[k-1] + postfix_stack[k] 
                address_table_arr[postfix_stack[k-1]] = index
                index += 1

                del postfix_stack[k]
            else:
                postfix_stack[k-2] = postfix_stack[k-2] + postfix_stack[k-1] + postfix_stack[k] 
                address_table_arr[postfix_stack[k-2]] = index
                index += 1

                del postfix_stack[k]
                del postfix_stack[k-1]
            
            k = -1
            

        k += 1 

    
    Truthtable = [] 
    i = len(table) -1
    while i >= 0:
        Truthtable.append(table[i])
        i -=1
    return Truthtable

# Postfix=Infix2Postfix("R|(P&Q)")
# Truthtable=Postfix2Truthtable(Postfix)
# print(Truthtable)
print(Infix2Postfix("R|(P&Q)"))
print(Infix2Postfix("~P|(Q&R)>R"))
print(Infix2Postfix("P|(R&Q)"))
print(Infix2Postfix("(P>Q)&(Q>R)"))
print(Infix2Postfix("(P|~Q)>~P=(P|(~Q))>~P"))


def Infix2Postfix(Infix):
    Postfix = ""
    logic1 = ["&", "|" , "~" ,  "("]
    operators =[]
    stack = []
    for i in Infix:
        if i in listAlphabet():
            stack.append(i)
            if len(operators) > 0 and operators[len(operators)-1] =='~':
                stack.append(operators[-1])
                operators.pop()
        else:
            if i in logic1: #["&", "|" , "~" ,  "("]
                operators.append(i)
            elif i==">" or i=="=" or i==")":
                if i == ")":
                    while(not(operators[len(operators)-1] == '(') ):
                        stack.append(operators[len(operators)-1])
                        operators.pop()
                    operators.pop()
                    if(len(operators) > 0):
                        stack.append(operators[len(operators)-1])
                        operators.pop()
                elif  i == ">" or i == "=":
                    operators.append(i)
    while len(operators) +1> 1:
        stack.append(operators[len(operators)-1])
        operators.pop()
    for i in range(0,len(stack)):
        Postfix += stack[i]
    return Postfix