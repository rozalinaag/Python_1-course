m,n,r = list(map(int, input().split()))
a=[0]*m
for i in range(m):
    ai=input()
    a[i]=ai.split()
b=[0]*n
for i in range(n):
    bi=input()
    b[i]=bi.split()
c=[0]*m
for i in range(m):
    c[i]=[0]*r
s=0
for i in range(m):
    for j in range(r):
        for k in range(n):
            a[i][k]=int(a[i][k])
            b[k][j]=int(b[k][j])
            s=s+a[i][k]*b[k][j]
        c[i][j]=s
        s=0
for i in range(m):
    for j in range(r):
        print(c[i][j], end=' ')
    print()
