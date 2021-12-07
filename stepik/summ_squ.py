a=int(input())
summ_square=0
summ=0
while(True):
    summ+=a
    summ_square+=a*a
    if (summ)==0:
        break
    a=int(input())
print(summ_square)
