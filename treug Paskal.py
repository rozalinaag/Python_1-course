def PasTri(n):
    import math
    def binomial(n,k):
        return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    
    if n==1:
        spis=[1]
        print(spis)
    elif n==2:
        spis=[1,1]
        print(spis)
    else:
        spis=[1]
        print(spis)
        print([1,1])
        for j in range(2,n):
            spis=[1]
            klop=j
            for i in range(1,klop,1):
                spis.append(int(binomial(klop,i)))
            spis.append(1)
            print(spis)
        


PasTri(6)
