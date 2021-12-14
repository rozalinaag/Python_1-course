"""Cистема проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка.На вход программе первой строкой передаётся количество d известных нам слов, 
после чего на d строках указываются эти слова. 
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра."""

n = int(input())
list_of_words = []
for i in range(n):
    list_of_words.append(input().lower())

l = int(input())
list_of_new_words = []
for i in range(l):
    line=input().lower().split()
    for j in line:
        list_of_new_words.append(j)
print(list_of_new_words)
dic = {}
for i in list_of_new_words:
    if i not in list_of_words:
        dic[i] = 1
for i in dic:
    print(i)

"""
dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")"""
