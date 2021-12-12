a = "For all fish, they need water to survive"
b = "Exist a person, who is left handed"
c = "Exist an employee in the company, who is late to work everyday."
d = "For all fish in this pond, they are Koi fish."
e = "There is at least one creature in the ocean, it can live on land"
def neGa(A):
    F=""
    tempF=""
    tempM=""
    tempL=""
    arr = A.split(',')
    #for all
    if arr[0].startswith("For all"):
        tempF = arr[0].replace("For all","Exist")
        tempM =" such that "
        tempL = arr[1].replace(" they ","they not ")
    if arr[0].startswith("Exist"):
        tempF = arr[0].replace("Exist","For all") 
        tempM = ","
        tempL = arr[1].replace(" who is ", " who isn't ")
    if arr[0].startswith("There is at least"):
        tempF = arr[0].replace("There is at least one","There is the most")
        tempM = ","
        tempL = arr[1].replace(" it can"," it can't")
    F = F + tempF + tempM + tempL
    return F
print(neGa(a))
print(neGa(b))
print(neGa(c))
print(neGa(d))
print(neGa(e))
