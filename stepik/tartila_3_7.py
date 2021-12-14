"""Группа биологов в институте биоинформатики завела себе черепашку.

После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
север 10
запад 20
юг 30
восток 40
где первое слово — это направление, в котором должна двигаться черепашка, а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.
Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, после чего nn строк с самими командами. Вывести нужно два числа в одну строку:
первую и вторую координату конечной точки черепашки. Все координаты целочисленные."""

n = int(input())
xy = [0,0]
for i in range(n):
    line = input().split()
    if line[0] == "север":
        xy[1] += int(line[1])
    elif line[0] == "юг":
        xy[1] -= int(line[1])
    elif line[0] == "восток":
        xy[0] += int(line[1])
    else:
        xy[0] -= int(line[1])
print(xy[0], xy[1])


#another decision 
"""n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    x=input().split()
    d[x[0]]+=int(x[1])
print(d['восток']-d['запад'], d['север']-d['юг'])"""
