#ex1
Andersen ={"The Emperor’s New Clothes","The Little Mermaid","The Little Match Girl", "The Snow Queen"}

#ex2
Shakespeare ={"Romeo andJuliet", "Hamlet", "King Lear", "Macbeth","A Midsummer Night’s Dream", "A Comedy ofErrors"}

#ex3
Tragedy ={"Medea", "Octavia", "Oedipus","Ur-Hamlet","Romeo andJuliet", "Hamlet", "King Lear","Macbeth"}
Comedy ={"The Three Musketeer", "The Clouds","A Midsummer Night’s Dream", "A Comedy ofErrors"}
Uncategory ={"Don Quixote", "Rapunzel", "Cinderella","The Emperor’s New Clothes","The Little Mermaid","The Little Match Girl", "The Snow Queen"}

#ex4
print("ex4:")
shakespeare_Tragedy = Shakespeare - Comedy
shakespeare_Tragedy1 = Shakespeare.difference(Comedy)
print(shakespeare_Tragedy1)
#in ra se dc random, hong co thu tu


#ex5
print("ex5:")
Andersen_Comedy = Andersen.intersection(Comedy) #c1
Andersen_Comedy1 = Andersen & Comedy #c2
print(Andersen_Comedy1)

#ex6
print("ex6:")
print("ktra Andersen_comedy issubset to per set")
print(Andersen_Comedy.issubset(Shakespeare))
print(Andersen_Comedy.issubset(Andersen))
print(Andersen_Comedy.issubset(Tragedy))
print(Andersen_Comedy.issubset(Comedy))
print(Andersen_Comedy.issubset(Uncategory))

print("ktra Andersen_comedy issuperset to per set")
print(Andersen_Comedy.issuperset(Shakespeare))
print(Andersen_Comedy.issuperset(Andersen))
print(Andersen_Comedy.issuperset(Tragedy))
print(Andersen_Comedy.issuperset(Comedy))
print(Andersen_Comedy.issuperset(Uncategory))

print("ktra Andersen_comedy isdisjoint to per set")
print(Andersen_Comedy.isdisjoint(Shakespeare))
print(Andersen_Comedy.isdisjoint(Andersen))
print(Andersen_Comedy.isdisjoint(Tragedy))
print(Andersen_Comedy.isdisjoint(Comedy))
print(Andersen_Comedy.isdisjoint(Uncategory))

print("ktra shakespeare_Tragedy issubset to per set")
print(shakespeare_Tragedy.issubset(Shakespeare))
print(shakespeare_Tragedy.issubset(Andersen))
print(shakespeare_Tragedy.issubset(Tragedy))
print(shakespeare_Tragedy.issubset(Comedy))
print(shakespeare_Tragedy.issubset(Uncategory))

print("ktra shakespeare_Tragedy issuperset to per set")
print(shakespeare_Tragedy.issuperset(Shakespeare))
print(shakespeare_Tragedy.issuperset(Andersen))
print(shakespeare_Tragedy.issuperset(Tragedy))
print(shakespeare_Tragedy.issuperset(Comedy))
print(shakespeare_Tragedy.issuperset(Uncategory))

print("ktra shakespeare_Tragedy isdisjoint to per set")
print(shakespeare_Tragedy.isdisjoint(Shakespeare))
print(shakespeare_Tragedy.isdisjoint(Andersen))
print(shakespeare_Tragedy.isdisjoint(Tragedy))
print(shakespeare_Tragedy.isdisjoint(Comedy))
print(shakespeare_Tragedy.isdisjoint(Uncategory))


#ex7
print("ex7:")
Work = Tragedy |Comedy|Uncategory
print(Work)


#ex8
print("ex8:")
Author = {"Andersen","Shakespeare","Unknown"}
#Unknown = (Work - Andersen) - Shakespeare
Unknown = Work.difference(Andersen.union(Shakespeare))
print(Unknown)

#ex9
print("ex9:")
Author_Of={}
for i in Andersen:
    Author_Of[i]='Andersen'
for i in Shakespeare:
    Author_Of[i] = 'Shakespeare'
for i in Unknown:
    Author_Of[i] = 'Unknown'
print(Author_Of)

#ex10 nguoc vs cau 9
print("Ex10: ")
Written_By={}
#c1
# for i in Andersen:
#     Written_By['Andersen'] = i
# for i in Shakespeare:
#     Written_By['Shakespeare'] = i
# for i in Unknown:
#     Written_By['Unknown'] = i

#c2
# for i in Author_Of:
#     for j in Work:
#         if Author_Of[j] == 'Andersen':
#             Written_By['Andersen'] = j
#         if Author_Of[j] == 'Shakespeare':
#             Written_By['Shakespeare'] = j
#         if Author_Of[j] == 'Unknown':
#             Written_By['Unknown'] = j

#c3
for i,j in Author_Of.items():
    Written_By[j] = i

print(Written_By)


#ex11
print("Ex11: ")
work_Count={}
count = 1
for i in Work:
    if i in Andersen:
        count+=1
    if i in Shakespeare:
        count+=1
    if i in Tragedy:
        count+=1
    if i in Comedy:
        count+=1
    if i in Uncategory:
        count+=1
    if i in Andersen_Comedy:
        count+=1
    if i in shakespeare_Tragedy:
        count+=1
    work_Count[i] = count
print(count)
print(work_Count)

