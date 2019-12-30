n=int(input())
d={}
M={}
masstr=[]
sumsim=0
for index in range(n):
    stroka = input()
    stroka=stroka.split()
    for i in range(len(stroka)):
        strokai=stroka[i]
        masstr.append(stroka[i])
        for k in range(len(strokai)):
            sumsim+=ord(strokai[k])
        d[stroka[i]]=sumsim
        sumsim=0
maxk=1
for i in range(len(masstr)):
        k=masstr.count(masstr[i])
        if k>maxk:
            maxk=k
for i in range(len(masstr)):
        k=masstr.count(masstr[i])
        if k==maxk:
            M[masstr[i]]=d[masstr[i]]
            sumsim=M[masstr[i]]
            minworld=masstr[i]
for key in M:
    if (sumsim>M[key]):
        sumsim=M[key]
        minworld=key
print(minworld)


