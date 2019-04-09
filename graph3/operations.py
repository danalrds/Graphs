class Graph():
    def __init__(self,nrV):
        self.__in={}
        self.__out={}
        self.__nrV=nrV
        self.__cost={}
        self.__father={}
        self.__nrPaths=0
        for i in range(0,nrV):
            self.__in[i]=[]
            self.__out[i]=[]
        maxint=9999999
        for i in range(0,nrV):
            for j in range(0,nrV):
                self.__father[(i,j)]=-1
                self.__cost[(i,j)]=maxint;
    '''input data: startVertex and endVertex, appends in inbound list and outbound list the correspondent vertex'''
    def addEdge(self,startVertex,endVertex,cost):
        #print(startVertex,endVertex)
        self.__cost[(startVertex,endVertex)]=cost
        if startVertex not in self.__in[endVertex]:
            self.__in[endVertex].append(startVertex)
        if endVertex not in self.__out[startVertex]:
            self.__out[startVertex].append(endVertex)
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
        print(self.__cost)
        if vertex in self.__in.keys():
            return self.__in[vertex]
        return []
    def RoyFloyd(self):
        for k in range(0,self.getNrV()):
            for i in range(0,self.getNrV()):
                for j in range(0,self.getNrV()):
                    costul=self.__cost[(i,k)] + self.__cost[(k,j)]
                    if self.__cost[(i,j)] > costul :
                            self.__cost[(i,j)]=costul
                            self.__father[(i,j)]=k
        #for key in self.__cost:
        #    if self.__cost[key] != 9999999:
        #        print(key, self.__cost[key])
        return self.__cost
    def getNrMinPaths(self,start,end):
        return self.__count[(start,end)]
    def traseu(self,x,y):
        if self.__father[(x,y)] != -1:
            k=self.__father[(x,y)]
            self.traseu(x,k)
            print(k)
            self.traseu(k,y)
    def printPaths(self,start,end,visited,path):
        visited[start]=True
        path.append(start)
        if start==end:
            self.__nrPaths=self.__nrPaths+1
            print(path)
        else:
            for i in self.outEdges(start):
                if visited[i]==False:
                    self.printPaths(i,end,visited,path)
        path.pop()
        visited[start]=False

    def showAllPaths(self,start,end):
        visited =[False]*(self.__nrV)
        self.__nrPaths=0
        paths=[]
        path=[]
        self.printPaths(start,end,visited,path)
        print("There are",self.__nrPaths,"distinct paths between",start,"and",end )
    def countPaths(self,value,start,end,visited,path):
        visited[start]=True
        path.append(start)
        if start==end:
            s=0
            for i in range(0,len(path)-1):
                s=s+self.__cost[(path[i],path[i+1])]
            if s==value:
                self.__nrPaths=self.__nrPaths+1
        else:
            for i in self.outEdges(start):
                if visited[i]==False:
                    self.countPaths(value,i,end,visited,path)
        path.pop()
        visited[start]=False

    def countAllPaths(self,value,start,end):
        visited =[False]*(self.__nrV)
        self.__nrPaths=0
        path=[]
        self.countPaths(value,start,end,visited,path)
        return  self.__nrPaths
