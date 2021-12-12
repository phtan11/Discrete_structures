#a
P="Phong has Visa"
S2 = "If Phong has Visa, Phong will go to American"
C ="Phong goes to American"
print("cau a:")
print(S2)
print(P)
print(C )
print("prove by ponens")
print()

#b
print("cau b")
print("Disprove")
S1="If it's hot,it will rain the next day."
P = "It's hot yesterday"
print(S1)
print(P)
print("today it's rain (1)" )
print()
S2 = "If and only if it's not rain, Name goes outside"
print(S2)
print("If name goes outside,then it doesn't rain (by specialization) (2)")
print()
print("if Name goes outside,then it doesn't rain (by 2)")
print("today it's rain (by 1)")
print("*Name doesn't go outside (by tollens)")
print()

#c
print("cau c")
print("Disprove")
P = "the traffic is flowing smooth"
S1 = "The traffic is always heavy on school day"
print("if it is on school day,then the traffic is always heavy (by S1) ")
print(P)
print("it's not on school day (by tollens) (1)")
print()

S3 ="An only have to go to school on school day"
print("An has to go to school if and only if it's school day(by S3)")
print("if An has to go to school,then it's on school day (by specialization)")
print("it's not on school day (by 1)")
print("An doesn't have to go school(by tollens) (2)")
print()

print("If An don't have to go to school, An can't be late for school (by S4) ")
print("An doesn't have to go school (by 2)")
print("An can't be late for school (by ponens)")
print()

