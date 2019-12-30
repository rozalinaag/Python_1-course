mas_strok=[]
stroka=input()
while (stroka!=''):
    mas_strok.append(stroka)
    stroka=input()
double_mas=[]
kolvo_ravn=0
for i in range(len(mas_strok)):
    for j in range(len(double_mas)):
        if mas_strok[i]==double_mas[j]:
            kolvo_ravn+=1
    if kolvo_ravn==0:
        double_mas.append(mas_strok[i])
    kolvo_ravn=0
for i in range(len(double_mas)):
    if double_mas!='':
        print(double_mas[i])
    else:
        break

            
    
