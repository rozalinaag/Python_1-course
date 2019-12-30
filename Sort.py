
n = int(input())
megostroka = ''
for index in range(n):
    megostroka += input()
    megostroka += ' '
dic = {}
kor = ()
megostroka = megostroka.split()
for i in range(len(megostroka)):
    k = megostroka.count(megostroka[i])
    word = megostroka[i]
    sumletters = 0
    for j in range(len(word)):
        sumletters += ord(word[j])
    lor = (k, megostroka[i])
    kor = kor + (lor,)
for i in range(len(kor)):
    dic[kor[i][1]] = kor[i][0]

dic = list(dic.items())

dic = sorted(dic, key=lambda check: (-check[1], check[0]), reverse=True)
for i in reversed(range(len(dic))):
    print(dic[i][0])
