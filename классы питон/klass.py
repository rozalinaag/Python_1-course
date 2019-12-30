class SocialNetwork(object):
    def __init__(self,file):
        spis=list(open(file,"r"))
        self.spis=spis
    def recommend(self,user_id):
        lost=self.spis
        kor=[]
        posl=lost[-1]
        for i in range(len(lost)-1):
            strok=lost[i]
            if i!=len(lost)-1:
                lo=strok[:len(strok)-1]
            klop=''
            klop2=''
            for j in range(len(lo)):
                if lo[j]!=' ':
                   klop+=lo[j]
                else:
                    klop2=lo[j+1:]
                    break
            if len(kor)>0:
                pus=(int(klop),int(klop2))
            else:
                pus=(int(klop),klop2)
            kor.append(pus)
        klop=''
        for j in range(len(posl)):
            if posl[j]!=' ':
                klop+=posl[j]
            else:
                klop2=posl[j+1:]
                break
        pus=(int(klop),int(klop2))
        kor.append(pus)
        ide=user_id
        podspis=[]
        for i in range(1,len(kor)):
            newklop=[]
            idd=kor[i][0]
            idd2=kor[i][1]
            f=0
            for s in range(len(podspis)):
                if podspis[s][0]==idd:
                    f=1
            if f==0:
                newklop.append(kor[i][0])
                for j in range(len(kor)):
                    if kor[j][0]==idd:
                        newklop.append(kor[j][1])
                    elif kor[j][1]==idd:
                        newklop.append(kor[j][0])
                podspis.append(newklop)
            f=0
            newklop=[]
            for s in range(len(podspis)):
                if podspis[s][0]==idd2:
                    f=1
            if f==0:
                newklop.append(kor[i][1])
                for j in range(len(kor)):
                    if kor[j][0]==idd2:
                        newklop.append(kor[j][1])
                    elif kor[j][1]==idd2:
                        newklop.append(kor[j][0])
                podspis.append(newklop) 
        maxkolvo=0
        kolvo=0
        for i in range(len(podspis)):
            if podspis[i][0]==ide:
                index=i
        for i in range(len(podspis)):
            friend=podspis[i]
            if friend[0]!=ide:
                if friend[0] not in podspis[index]:
                    for k in range(1,len(friend)):
                        if friend[k] in podspis[index]:
                            kolvo+=1
                    podspis[i].append('*')
                    podspis[i].append(kolvo)
            if kolvo>maxkolvo:
                maxkolvo=kolvo
            kolvo=0
        gotovo=[]
        for i in range(len(podspis)):
            friend=podspis[i]
            if friend[0]!=ide:
                if friend[0] not in podspis[index]:
                    if friend[-1]==maxkolvo:
                        gotovo.append(friend[0])
        gotovo.sort()
        return gotovo[0]
alfa=SocialNetwork("small_net.TXT")
print(alfa.recommend(1))


