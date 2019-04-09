class Graph():
    def __init__(self,nrV):
        self.__in={}
        self.__out={}
        self.__nrV=nrV
        self.__suc=[]
        self.__pred=[]
        self.nrC=1
        self.Time = 0
        self.count = 0
        for i in range(0,nrV):
            self.__in[i]=[]
            self.__out[i]=[]
            self.__suc.append(0)
            self.__pred.append(0)
    '''input data: startVertex and endVertex, appends in inbound list and outbound list the correspondent vertex'''
    def addEdge(self,startVertex,endVertex):
        #print(startVertex,endVertex)
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
        if vertex in self.__in.keys():
            return self.__in[vertex]
        return []

    def bf(self,start,end):
        c=[]
        distance={}
        c.append(end)
        distance[end]=0
        while c != []:
            vertex=c[0]
            c.pop(0)
            for i in self.inEdges(vertex):
                if i not in distance.keys():
                    distance[i]=distance[vertex]+1
                    c.append(i)
        if start not in distance.keys():
            return None
        return distance[start]

    def df_r1(self,nod):
        self.__suc[nod]=self.nrC
        for i in self.outEdges(nod):
            if self.__suc[i]==0:
                self.df_r1(i)
    def df_r2(self,nod):
        self.__pred[nod]=self.nrC
        for i in self.inEdges(nod):
            if self.__pred[i]==0:
                self.df_r2(i)
    def compConex(self):
        for i in range(0,self.getNrV()):
            if self.__suc[i]==0:
                self.__suc[i]=self.nrC;
                self.df_r1(i)
                self.df_r2(i)
                for j in range(0,self.getNrV()):
                    if self.__suc[j]!=self.__pred[j]:
                        self.__suc[j]=0
                        self.__pred[j]=0
                self.nrC=self.nrC+1
        for i in range(1,self.nrC):
            print("Componenta", i, ":")
            for j in range(0,self.__nrV):
                if self.__suc[j]==i:
                    print(j)
    def BCCUtil(self,u, parent, low, disc, st):
        children =0
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.__out[u]:
            if disc[v] == -1 :
                parent[v] = u
                children += 1
                st.append((u, v)) #store the edge in stack
                self.BCCUtil(v, parent, low, disc, st)
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])
                # If u is an articulation point,pop
                # all edges from stack till (u, v)
                if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]:
                    self.count +=1 # increment count
                    w = -1
                    list=[]
                    while w != (u,v):
                        w = st.pop()
                        if w[0] not in list:
                            list.append(w[0])
                        if w[1] not in list:
                            list.append(w[1])
                        #print(w)
                    list.sort()
                    print(list)

            elif v != parent[u] and low[u] > disc[v]:
                low[u] = min(low [u], disc[v])
                st.append((u,v))

    def BCC(self):
        # Initialize disc and low, and parent arrays
        nrV=self.getNrV()
        disc = [-1] * (nrV)
        low = [-1] * (nrV)
        parent = [-1] * (nrV)
        st = []
        # Call the recursive function to
        # find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.getNrV()):
            if disc[i] == -1:
                self.BCCUtil(i, parent, low, disc, st)
            #If stack is not empty, pop all edges from stack
            if st:
                self.count = self.count + 1
                list=[]
                while st:
                    w = st.pop()
                    if w[0] not in list:
                        list.append(w[0])
                    if w[1] not in list:
                        list.append(w[1])
                    #print(w)
                list.sort()
                print(list)


    def df(self,start,viz):
        viz.append(start)
        for i in self.outEdges(start):
            if i not in viz:
                self.df(i,viz)
        return viz
