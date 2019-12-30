stroka=input()
k=0
f=0
a=0
A=0
for i in range(26):
    for j in range(len(stroka)):
        if (stroka[j]==chr(a+97)or stroka[j]==chr(A+65)) and f==0:
            k+=1
            f=1
    a+=1
    A+=1
    f=0
print(k)       
if k==26:
    print('yes')
else:
    print()
 
