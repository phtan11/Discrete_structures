def Choice():
    p="it sunny"
    q="i go camping"
    option=input("Enter your logic statement:")
    if(option == "if p then q"):
        return "if "+p+",then "+q
    elif(option== "p, and not q"):
        return "it sunny and I not go camping"
    elif(option== "not p, or q"):
        return "it not sunny or I go camping"
print(Choice())