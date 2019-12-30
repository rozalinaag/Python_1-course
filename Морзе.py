stroka=input()
masstrok=[]
while stroka!='@':
    masstrok.append(stroka)
    stroka=input()
dic={}
dic['a']='.-'
dic['b']='-...'
dic['c']='-.-.'
dic['d']='-..'
dic['e']='.'
dic['f']='..-.'
dic['g']='--.'
dic['h']='....'
dic['i']='..'
dic['j']='.---'
dic['k']='-.-'
dic['l']='.-..'
dic['m']='--'
dic['n']='-.'
dic['o']='---'
dic['p']='.--.'
dic['q']='--.-'
dic['r']='.-.'
dic['s']='...'
dic['t']='-'
dic['u']='..-'
dic['v']='...-'
dic['w']='.--'
dic['x']='-..-'
dic['y']='-.--'
dic['z']='--..'
dic['0']='-----'
dic['1']='.----'
dic['2']='..---'
dic['3']='...--'
dic['4']='....-'
dic['5']='.....'
dic['6']='-....'
dic['7']='--...'
dic['8']='---..'
dic['9']='----.'
kod=''
stkod=''
gotovo=[]
for index in range(len(masstrok)):
    prover=masstrok[index]
    if prover[0]!='-' and prover[0]!='.':
        for i in range(len(prover)):
            if prover[i]==' ':
                kod+='p'
            for key in dic:
                up=prover[i].upper()
                low=prover[i].lower()
                if prover[i]==key or up==key or low==key:
                    kod+=dic[key]+' '
        gotovo.append(kod)
        kod=''
    else:
        prover=prover.split()
        for j in range(len(prover)):
            if prover[j]=='p':
                stkod+=' '
            for key in dic:
                if prover[j]==dic[key]:
                    stkod+=key
        gotovo.append(stkod)
        stkod=''
for i in range(len(gotovo)):
    print(gotovo[i])
        
        
    
