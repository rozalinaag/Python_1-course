"""Программа должна считывать размеры команд
(два положительных целых числа a и b, каждое число вводится на отдельной строке) 
и выводить наименьшее число d, которое делится на оба этих числа без остатка."""

a = int(input())
b = int(input())
d = a
while d%b:
    d += a
print(d)
