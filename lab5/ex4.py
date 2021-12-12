#a
print("cau a")
print("Prove")
print("S2=If Phong has Visa, Phong will go to America")
print("p->t (S2)")
print("p (P)")
print("t (by ponens)")

#b
print("cau b")
print("Disprove")
print("S1=The traffic is always heavy on school day")
print("if it is on school day,then the traffic is always heavy (by S1) ")
print("r->~q")
print("q")
print("~r (by tollens) (1)")
print()

S3 ="An only have to go to school on school day"
print("An has go to school if and only if it's school day (by S3) ")
print("if An has to go to school,then it't on school day(by specialization)")
print("s->r")
print("~r (by 1)")
print("~s (by tollens) (2)")
print()
S4="If An don’t have to go to school, An can’t be late for school"
print("~s->~v")
print("~s(by 2)")
print("~v(by ponens)")