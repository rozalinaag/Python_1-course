n = int(input())
a=[0]*n
for i in range(n):
    a[i]=[0]*n
for i in range(n):
    for j in range(n):
       a[i][i]=0
for i in range(n):
    for j in range(n):
        a[i][j] = abs(j - i)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
