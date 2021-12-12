
def richest(x):
    if len(x)==1:
        return x[0]
    # C1 : return max(richest(x[0:len(x)-2]),x[len(x)-1]) #ptu cuoi voi tu dau den gaan cuoi
    return max(richest(x[1:]),x[0]) # xet ptu dau roi ptu tiep theo den cuoi

print(richest([1,7,2,8,38]))