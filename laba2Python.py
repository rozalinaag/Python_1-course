import random
kolvo=0
ik1=0
ik0=0
n=0
f=0
s=''
i=0
m=''
srednee=0
alist=['','','','','','','','','','']
while(n!=11):
    while(f==1):
        a=random.randint(0, 1)
        if (a==1):
            s=s+'T'
        else:
            s=s+'H'
        kolvo+=1
        if (a==1):
            ik1+=1
            ik0=0
        else:
            ik0+=1
            ik1=0
        if (ik1==3 or ik0==3):
            f=0
            srednee+=kolvo
            m=str(kolvo)
            alist[i]=s+' '+m
            i+=1
            m=''      
            
    n+=1
    f=1
    ik1=0
    ik0=0
    s=''
    kolvo=0
for i in range(10):
    print(alist[i])
print(srednee/10)
