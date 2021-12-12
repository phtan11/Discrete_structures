def thieves(x):
    if(x==1):
        return 1
    if x==2:
        return 2
    sum = x
    for i in range(1,x):
        sum += thieves(i)
    return sum
    
def countDay():
    count = 0
    THIEVES = 40
    while THIEVES >0:
        count += 1
        THIEVES -= thieves(count)
    return count-1

print(thieves(6))
print(countDay())