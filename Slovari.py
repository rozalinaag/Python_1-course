nm=input()
nm=nm.split()
n=int(nm[0])
m=int(nm[1])
dicKlav={}
dicSvet={}
alldic={}
for i in range(n):
    a=int(input())
    dicKlav[a]=0
for i in range(m):
    a=int(input())
    dicSvet[a]=0
onlyKlava={}
onlySveta={}
for key in dicKlav:
    k=0
    for svet in dicSvet:
        if svet==key:
            k=1
            alldic[key]=0
    if (k==0):
        onlyKlava[key]=0
for key in dicSvet:
    k=0
    for svet in dicKlav:
        if svet==key:
            k=1
    if (k==0):
        onlySveta[key]=0
onlyKlava=list(onlyKlava.keys())
onlyKlava.sort()
onlySveta=list(onlySveta.keys())
onlySveta.sort()
alldic=list(alldic.keys())
alldic.sort()
print(len(alldic))
if len(alldic)==0:
    print()
for i in range(len(alldic)):
    print(alldic[i])
print(len(onlyKlava))
if len(onlyKlava)==0:
    print()
for i in range(len(onlyKlava)):
    print(onlyKlava[i])
print(len(onlySveta))
for i in range(len(onlySveta)):
    print(onlySveta[i])









