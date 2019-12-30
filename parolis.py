parol=input()
a=0
A=0
number=0
simbol=0
if len(parol)<6 or len(parol)>12:
    print()
else:
    for i in range(len(parol)):
        for j in range(26):
            if parol[i]==chr(j+97):
                a+=1
            if parol[i]==chr(j+65):
                A+=1
        if parol[i].isdigit():
            number+=1
        if parol[i]=='@' or parol[i]=='#' or parol[i]=='$':
            simbol+=1
    if (simbol>0 and a>0 and A>0 and number>0):
        print(parol)
