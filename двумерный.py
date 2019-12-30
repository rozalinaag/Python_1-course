n=int(input())
mass=[0]*n
for i in range(n):
    mass[i]=[0]*n
for i in range(n):
    for j in range(n):
       mass[i][i]=0
k=1
l=0
l1=0
l2=1
ki=l1
kj=l2
for i in range(2):
    for j in range(n-1):
           if (i<j):
               mass[ki][kj]=1
               ki+=1
               kj+=1
    l2+=1
    l+=1

    

           
           
for i in range(n):
    for j in range(n):
        print(mass[i][j], end=' ')
    print()
    
