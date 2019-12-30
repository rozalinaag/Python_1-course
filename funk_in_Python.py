def isPerfectNumber(n):
    samsa=0
    if n>0:
        for i in range(1,n,1):
            if n%i==0:
                samsa+=i
    elif n<0:
        for i in range(n+1,0,1):
            if n%i==0:
                samsa+=i
    if samsa==n and n!=0:
        return True
    else:
        return False



