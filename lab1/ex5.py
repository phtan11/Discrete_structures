def calculate(a,b,ope):
    if(ope == "+"):
        return a+b
    if(ope == "-"):
        return a-b
    if(ope == "*"):
        return a*b
    if(ope == "/"):
        return a/b
    if(ope == "%"):
        return a%b
    if(ope == "^"):
        return a**b
operator = input('input operator are:')
z = calculate(2,3,operator)
if(operator == "/" or operator or "%"):
    print("%f" %z)
else:
    print("%d" %z)
