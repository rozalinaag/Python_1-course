class Graph():
    def loadfromfile(self,name):
        self.spis=list(open(name,'r'))

    def dijkstra_shortest_path(self,u):
        chislo_vertex=int(self.spis[0])
        name=self.spis[1]
        name=name.split()
        matr_vesov=[]
        for i in range(2,len(self.spis)):
            stroka=self.spis[i]
            stroka=stroka.split()
            for j in range(len(stroka)):
                stroka[j]=int(stroka[j])
            matr_vesov.append(stroka)
            
        vertex=[]  #названия вершин
        for i in range(chislo_vertex): #преобразовываем названия 'name','name_two'
            lob=name[i]
            f=0
            klop=''
            for j in range(len(lob)):
                if f==1 and lob[j]!=',':
                    klop+=lob[j]
                if lob[j]==':':
                    f=1
            vertex.append(klop)
        
        for i in range(len(vertex)):  #находим индекс отталкивающей вершины
            if u==vertex[i]:
                index_u=i

        kor=[]
        lob=[index_u,0]
        kor.append(lob)  #добавляем первую вершину в готовый список кор
        
        
        matr_pred=[]  #предыдущая строка в построительной матрицы
        for i in range(chislo_vertex): #делаем главную вершину 0 остальные 10000
            a=1000000
            if i==index_u:
                a='+'
                matr_pred.append([i,a])
            else:
                matr_pred.append([i,a])
            
        matr_new=[] #новая строка в построительной матрицы
        for i in range(chislo_vertex):
            matr_new.append(matr_pred[i])  #copy matr_pred in matr_new

        def funkshion(matr_vesov,matr_pred,matr_new,index_u):
            for i in range(len(matr_vesov)): #заполнение значениями на первой итерац
                if i==index_u:
                    lob=matr_vesov[i] #[0,10,3,0]
                    for j in range(len(lob)):
                        if lob[j]>0:
                            for m in range(len(kor)):
                                if kor[m][0]==index_u:
                                    thnachen=kor[m][1]  
                            krot=lob[j]+thnachen  #10
                            if matr_pred[j][1]!='+' and krot<matr_pred[j][1]:
                                matr_new[j][1]=krot
            return matr_new

        matr_new=funkshion(matr_vesov,matr_pred,matr_new,index_u)
        
        #проверка на то, что есть не + вершины, значит будем дальше делать
        kolvo=0
        for i in range(len(matr_new)):
            if matr_new[i][1]!='+':
                kolvo+=1    #kolvo=3
                
        matr_pred=matr_new
        
        while(kolvo>0):
            minimum=100000
            for i in range(len(matr_new)):
                if matr_new[i][1]!='+' and matr_new[i][1]<minimum:
                    minimum=matr_new[i][1]
                    index_min=i
            index_u=index_min  #индекс новой вершины
            #надо отметить ее + и занести в список кор
            kor.append([index_u,minimum]) #[[0, 0], [2, 3]]

            for i in range(len(matr_pred)):
                if i==index_u:
                    matr_pred[i][1]='+'   #matr_pred=[[0, '+'], [1, 10], [2, '+'], [3, 1000000]]
                    matr_new[i][1]='+'

            #проверка на то, что есть не + вершины, значит будем дальше делать
            kolvo=0
            for i in range(len(matr_new)):
                if matr_new[i][1]!='+':
                    kolvo+=1  

            if kolvo>0:
                matr_new=funkshion(matr_vesov,matr_pred,matr_new,index_u) #matr_new = [[0, '+'], [1, 7], [2, '+'], [3, 14]]

            kolvo=0
            for i in range(len(matr_new)):
                if matr_new[i][1]!='+':
                    kolvo+=1
                    
        self.matr_vesov=matr_vesov
        self.vertex=vertex
        print(kor)
        return kor

    def dijkstra_get_path(self,u,v,l): #поиск индексов u and v
        for i in range(len(self.vertex)):
            if self.vertex[i]==u:
                index_u=i
            if self.vertex[i]==v:
                index_v=i    #1
        
        l.sort()
        gotovo=[]
        gotovo.append(self.vertex[index_v])
        index_pred=4
        klop=self.matr_vesov[index_v]
        def func(self,index_v,klop):
            for i in range(len(klop)):
                if klop[i]>0:
                    lob=l[i][1]+self.matr_vesov[i][index_v]
                    if lob==l[index_v][1]:
                        gotovo.append(self.vertex[i])
                        return i
        inn=index_v
        while (inn!=index_u and inn!=None):
            klop=self.matr_vesov[inn]
            inn=func(self,inn,klop)
            if inn==None:
                gotovo.append(self.vertex[index_u])
                inn=None
        gotovo.reverse()
        klop=''
        for i in range(len(gotovo)):
            klop+=gotovo[i]
            if i!=len(gotovo)-1:
                klop+='->'
        klop+=' ('+str(l[index_v][1])+')'
        print(klop)
        
        
G = Graph()
G.loadfromfile('2.txt')
l = G.dijkstra_shortest_path('x1')
G.dijkstra_get_path('x1', 'x2', l)



