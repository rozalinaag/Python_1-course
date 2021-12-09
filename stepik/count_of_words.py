"""подается строка, сколько слов и какое количество раз встречаются в ней без учета регистра"""


stroka =input().lower().split()
dic ={}
for i in stroka:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in dic:
    print(i, dic[i])
