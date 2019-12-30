n=int(input())
megostroka=''
for index in range(n):
    megostroka+=input()
    megostroka+=' '
dic={}
kor=()
megostroka=megostroka.split()
for i in range(len(megostroka)):
    k=megostroka.count(megostroka[i])
    word=megostroka[i]
    sumletters=0
    for j in range(len(word)):
        sumletters+=ord(word[j])
    lor=(k,megostroka[i])
    kor=kor+(lor,)
kor=sorted(kor)
for i in range(len(kor)):
    dic[kor[i][1]]=kor[i][0]
    
dic=list(dic.items())
lendic=len(dic)-1
mass=[]
while(lendic>-1):
    thnach=dic[lendic][1]
    index=lendic
    f=0
    while index!=0 and thnach==dic[index-1][1]:
        index-=1
        f=1
    ki=lendic
    if f==1:
        for j in range(index,ki+1):
            mass.append(dic[j][0])
        lendic=index-1
    else:
        mass.append(dic[lendic][0])
        lendic-=1
for i in range(len(mass)):
    print(mass[i])
