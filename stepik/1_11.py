"""Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное),
выводящее это число в консоль вместе с правильным образом изменённым словом "программист", 
для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
В комнате может быть очень много программистов. до 1000 человек."""

i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)
