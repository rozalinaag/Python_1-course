stroka=input()
X=['A','B','E','K','M','H','O','P','C','T','Y','X']
N=['0','1','2','3','4','5','6','7','8','9']
flagX=0
flagN=0
if len(stroka)>9 or len(stroka)<8:
    print('no')
else:
    for i in range(len(stroka)):
        if i==0 or i==4 or i==5:
            for j in range(len(X)):
                if stroka[i]==X[j]:
                    flagX+=1
        else:
            for j in range(len(N)):
                if stroka[i]==N[j]:
                    flagN+=1
    if (len(stroka)==9 and flagN==6 and flagX==3) or (len(stroka)==8 and flagN==5 and flagX==3):
        print('yes')
    else:
        print('no')
        
