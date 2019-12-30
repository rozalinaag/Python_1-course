def isSorted(lst):
    monrost=0
    monub=0
    if len(lst)>=2 and lst[0]<=lst[1]:
        monrost=1
        for i in range(len(lst)-1):
            if lst[i]<=lst[i+1] and monrost==1:
                monrost=1
            else:
                monrost=0
    if monrost==0:
        monub=1
        for i in range(len(lst)-1):
            if lst[i]>=lst[i+1] and monub==1:
                monub=1
            else:
                monub=0
    if monub+monrost>0:
        print(True)
    else:
        print(False)
isSorted([1,2,3,4])
