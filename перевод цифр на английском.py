from sys import stdin
lines = stdin.read().splitlines() 
app=[]
dic={}
only=[]
for i in range(len(lines)):
    k=0
    masworld=lines[i]
    masworld=masworld.split()
    for j in range(len(app)):
        if app[j]==masworld[0] and app[j+1]==masworld[1]:
            app[j+2]=int(app[j+2])
            masworld[2]=int(masworld[2])
            app[j+2]+=masworld[2]
            k=1
    if k==0:
        app.append(masworld[0])
        app.append(masworld[1])
        app.append(masworld[2])
        f=0
        for lk in range(len(only)):
            if only[lk]==masworld[0]:
                f=1
        if f==0:
            only.append(masworld[0])
    i+=3
only=sorted(only)
tovar=[]
gotovo=[]
for j in range(len(only)):
    for i in range(len(app)):
        if app[i]==only[j]:
            tovar.append(app[i+1])
    tovar=sorted(tovar)
    gotovo.append(only[j])
    for i in range(len(app)):
        if app[i]==only[j]:
            index=tovar.index(app[i+1])
            tovar.insert(index+1,app[i+2])
    gotovo.append(tovar)
    tovar=[]
for i in range(0,len(gotovo),2):
    print(gotovo[i],':',sep='')
    klop=gotovo[i+1]
    for j in range(0,len(klop),2):
        print(klop[j], klop[j+1])
    

    
           
