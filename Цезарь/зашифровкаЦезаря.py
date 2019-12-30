def caesarEncrypt(message, key, source="string"):
    if source!="file":
        letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        lob=""
        key=key%26
        for i in range(len(message)):
            klop=message[i]
            f=0
            for j in range(len(letter)):
                if f==0 and klop==letter[j]:
                        if j+key>=len(letter):
                            kolkon=len(letter)-j
                            newkey=key-kolkon
                            lob=lob+letter[newkey]
                            f=1
                        else:
                            lob=lob+letter[j+key]
                            f=1
                elif f==0 and klop==letter[j].upper():
                        if j+key>=len(letter):
                            kolkon=len(letter)-j
                            newkey=key-kolkon
                            lob=lob+letter[newkey].upper()
                            f=1
                        else:
                            lob=lob+letter[j+key].upper()
                            f=1
            if f==0:
                lob=lob+klop
        return lob
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
                            if j+key>=len(letter):
                                kolkon=len(letter)-j
                                newkey=key-kolkon
                                lob=lob+letter[newkey]
                                f=1
                            else:
                                lob=lob+letter[j+key]
                                f=1
                        elif f==0 and klop==letter[j].upper():
                            if j+key>=len(letter):
                                kolkon=len(letter)-j
                                newkey=key-kolkon
                                lob=lob+letter[newkey].upper()
                                f=1
                            else:
                                lob=lob+letter[j+key].upper()
                                f=1
                    if f==0:
                        lob=lob+klop
            return lob
        except:
            return "Can't open file "+message
            

print(caesarEncrypt("asadfgh,dfgh", 2,"file"))
