def caesarEncrypt(message, key, source):
    if source!="file":
        print('e')
    else:
        key=key%26
        letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        lob=""
        try:
            spis=list(open(message,'r'))
            for i in range(len(spis)):
                rubi=spis[i]
                for k in range(len(rubi)):
                    f=0
                    klop=rubi[k]
                    for j in range(len(letter)):
                        if f==0 and klop==letter[j]:
                            if j-key<=0:
                                pered=j
                                newkey=key-pered
                                lob=lob+letter[-newkey]
                                f=1
                            else:
                                lob=lob+letter[j-key]
                                f=1
                        elif f==0 and klop==letter[j].upper():
                            if j-key<=0:
                                pered=j
                                newkey=key-pered
                                lob=lob+letter[-newkey].upper()
                                f=1
                            else:
                                lob=lob+letter[j-key].upper()
                                f=1
                    if f==0:
                        lob=lob+klop
            return lob
        except:
            return "Can't open file "+message
            
def getFreq(file):
    spis=list(open(file,'r'))
    bigstroka=""
    lenka=len(spis)//4
    for k in range(lenka): #преобразовываем все в большую строку
        bigstroka+=spis[k]
    spisok=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    spisok2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    dic={}  
    bukvi=0  #количество букв всего в тексте (счетчик)
    lob="" #строка для составления вывода буква_процент_частота
    mop=0  #чтобы в конце не было лишний отступов при выводе
    for n in range(len(spisok)):
        for i in range(len(bigstroka)):
            up=spisok[n].upper()
            low=spisok[n].lower()
            if bigstroka[i]==up or bigstroka[i]==low:
                spisok2[n]+=1
                bukvi+=1
    list_dic=[]
    for i in range(len(spisok)):
        a=(spisok[i],spisok2[i])
        list_dic.append(a)
    
    list_dic.sort(key=lambda i: i[1], reverse=True)
            
    return list_dic

def keyk(letter_dic,letter_dic2):
        spisok=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(spisok)):
            if letter_dic==spisok[i]:
                index_dic=i+1
            if letter_dic2==spisok[i]:
                index_dic2=i+1
        if index_dic<index_dic2:
            key=index_dic2-index_dic
        else:
            kon=len(spisok)-index_dic
            key=kon+index_dic2
        return key
    
def breakCaesar(file, clean_text, dictionary = None):
    dic=getFreq(clean_text)
    dic2=getFreq(file)
    
    kolvo=0
    keykey=0
    while kolvo<1:
        kolvo=0
        key=keyk(dic[keykey][0],dic2[0][0])
        lob=caesarEncrypt(file, key, source="file")
        line=lob.split()
        keykey+=1
        with open(dictionary) as f:
            for more in f:
                if more==line[0].upper()+'\n' or more==line[1].upper()+'\n' or more==line[2].upper()+'\n' or more==line[3].upper()+'\n':
                    kolvo+=1
                if kolvo>1:
                    break
        if kolvo>0:
            break
    print(key)
    print(lob)
breakCaesar("cipher.TXT", "pg1741.TXT", "dictionary.txt")

