stroka=input()
k=0
a=stroka[0]
if (a.upper()==a):
    k+=1
    print(k)
if(stroka[1].upper()==stroka[1]):
    k+=1
    print(k)
if(stroka[2].upper()==stroka[2]):
    k+=1
    print(k)
if(stroka[3].upper()==stroka[3]):
    k+=1
    print(k)
if (k>=2):
    print(stroka.upper())
else:
    sim=stroka[-1]
    sim=sim.upper()
    print(stroka[:len(stroka)-1]+sim)
