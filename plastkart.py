def rle(a,i=0,spis=[]):
    def acva(a,k):
        if k<len(a)-1 and a[k]==a[k+1]:
            return acva(a,k+1)
        else:
            return k
    k=i 
    klop=acva(a,k)
    if i<len(a):
        spis.append(a[i])
    spis.append(klop-i+1) 
    if klop<=len(a):
        return rle(a,i=klop+1)
    else:
        spis.pop()
        spis.pop()
        return spis
print(rle('asssssddd'))
    
