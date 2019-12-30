NK=input()
NK=NK.split()
N=int(NK[0])
K=int(NK[1])
kegli=['|']*N
liri=[0]*K
for i in range(K):#двумерный массив лири
    liri[i]=[0]*2    
for i in range(K):
    liri_stroka=input()        #преобразовывание строки в числа 
    liri_mass=liri_stroka.split()
    li=int(liri_mass[0])
    ri=int(liri_mass[1])         # вот до сюда преобразовывание 
    liri[i][0]=li
    liri[i][1]=ri
for i in range(K):
    for j in range(liri[i][0]-1,liri[i][1]):
        kegli[j]='.'
for i in range(len(kegli)):
    print(kegli[i],end='')
        
        

