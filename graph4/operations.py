class Graph():
    def __init__(self,nrV):
        self.__in={}
        self.__cost=[]
        self.__out={}
        self.__nrV=nrV
        self.__parse={}
        self.__cos={}
        self.__t={}
        for i in range(0,nrV):
            self.__in[i]=[]
            self.__out[i]=[]
            self.__parse[i]=[]

    '''input data: startVertex and endVertex, appends in inbound list and outbound list the correspondent vertex'''
    def addEdge(self,startVertex,endVertex,cost):
        #print(startVertex,endVertex)
        self.__cost.append((startVertex,endVertex,cost))
        self.__cos[(startVertex,endVertex)]=cost
        self.__cos[(endVertex,startVertex)]=cost
        self.__parse[startVertex].append(endVertex)
        self.__parse[endVertex].append(startVertex)

        #if startVertex not in self.__in[endVertex]:
            #self.__in[endVertex].append(startVertex)
        #if endVertex not in self.__out[startVertex]:
            #self.__out[startVertex].append(endVertex)
    '''get number of vertices function: retuns the number of vertices of the graph'''
    def getNrV(self):
        return self.__nrV
    '''isEdge function, input data: start and end, 2 vertices, returns 1 if there is an edge, 0 otherwise'''
    def isEdge(self,start,end):
        ok=0
        for i in self.__in[end]:
            if i==start:
                ok=1
        return ok
    '''returns the list of outbound edges'''
    def outEdges(self,vertex):
        if vertex in self.__out.keys():
            return self.__out[vertex]
        return []
    '''returns the list of inbound edges'''
    def inEdges(self,vertex):
        if vertex in self.__in.keys():
            return self.__in[vertex]
        return []
    def father(self,node):
        if self.__t[node]<0:
            return node
        else:
            self.__t[node]=self.father(self.__t[node])
            return self.__t[node]
    def Kruskal(self):
        self.__cost=sorted(self.__cost, key=lambda x:x[2])
        #print(self.__cost)
        for i in range(self.__nrV):
            self.__t[i]=-1
        nr=0
        i=0
        res=[]
        sum=0
        for elem in self.__cost:
            start=elem[0]
            end=elem[1]
            cost=elem[2]
            a=self.father(start)
            b=self.father(end)
            if (a!=b):
                self.__t[b]=a
                nr=nr+1
                res.append(elem)
                sum=sum+cost
            i=i+1
        print("The cost of the minimum spanning tree is ",sum)
        print("The number of edges is ",nr) #or n-1 all the time
        print("Edges:")
        for i in range(nr):
            print(self.__cost[i][0],"~",self.__cost[i][1])
        return res
    def df(self,nod,viz,source,rez):
        viz.append(nod)
        rez.append(nod)
        for i in self.__parse[nod]:
            if i in viz:
                if (i in self.__parse[source]):
                    return
            else:
                self.df(i,viz,source,rez)
    def compute(self,rez):
        s=0
        for i in range(len(rez)-1):
            s=s+self.__cos[(rez[i],rez[i+1])]
        return s
