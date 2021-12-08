
"""Выведите матрицу размером n*n, заполненную числами от 1 до n^2  
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке"""


n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
f1, f2,m1,m2 = 1, 0,0,0
max_n, min_n = n-1, 0
for i in range(1, n*n+1):
    matrix[m1][m2] = i
    if f1==1 and f2==0:
        if m2<max_n:
            m2+=1
        else:
            f2+=1
            m1+=1
    elif f1==1 and f2==1:
        if m1<max_n:
            m1+=1
        else:
            f1+=1
            m2-=1
    elif f1==2 and f2==1:
        if (m2>0):
            m2-=1
        else:
            f2+=1 #m2==0
            min_n=1
            m1-=1
    elif f1==f2 and f1%2==0:
        if (m1>min_n):
            m1-=1
        else:
            f1+=1
            m2+=1
            max_n-=1
    elif f1>f2 and f2%2==0:
        if (m2<max_n):
            m2+=1
        else:
            f2+=1
            m1+=1
    elif f1==f2 and f1%2!=0:
        if (m1<max_n):
            m1+=1
        else:
            f1+=1
            m2-=1
    elif f1>f2 and f2%2!=0:
        if m2>min_n:
            m2-=1
        else:
            f2+=1
            min_n+=1
            m1-=1
for k in range(n):
    print(*matrix[k])


