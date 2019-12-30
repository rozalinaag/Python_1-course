stroka=input()
mass=stroka.split()
k=0
for i in range(len(mass)):
    for j in range (i+1,len(mass)):
        if (mass[i]==mass[j]):
            k+=1
print(k)
    
        
