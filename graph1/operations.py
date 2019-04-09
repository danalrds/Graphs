from EdgeProperty import *
class Graph():
    def __init__(self,nrV):
        self.__in={}
        self.__out={}
        self.__nrV=nrV

        for i in range(0,nrV):
            self.__in[i]=[]
            self.__out[i]=[]
    '''get number of vertices function: retuns the number of vertices of the graph'''
    def getNrV(self):
        return self.__nrV
    '''input data: the vertex to be added, creates empty lists for in and out vertices, increases the number of vertices '''
    def addVertex(self,Vertex):
        self.__in[Vertex]=[]
        self.__out[Vertex]=[]
        self.__nrV+=1;
    '''input data: the vertex to be removed, deletes the given vertex from inbound list and outbound list and creates another list with the edges '''
    '''to be removed from EdgeProperty after this operation'''
    def removeVertex(self,Vertex):
        list_remove=[]
        for x in self.__in[Vertex]:
            self.__out[x].remove(Vertex)
            list_remove.append((x,Vertex))
        for x in self.__out[Vertex]:
            self.__in[x].remove(Vertex)
            list_remove.append((Vertex,x))
        del self.__in[Vertex]
        del self.__out[Vertex]
        self.__nrV-=1;
        return list_remove
    '''input data: startVertex and endVertex, appends in inbound list and outbound list the correspondent vertex'''
    def addEdge(self,startVertex,endVertex):
        #print(startVertex,endVertex)
        if startVertex not in self.__in[endVertex]:
            self.__in[endVertex].append(startVertex)
        if endVertex not in self.__out[startVertex]:
            self.__out[startVertex].append(endVertex)
    '''input data: startVertex, endVertex, removes an edge by deleting from both inbound list and outbound list'''
    def removeEdge(self,startVertex,endVertex):
        for x in self.__in[endVertex]:
            if x==startVertex:
                self.__in[endVertex].remove(x)
        for x in self.__out[startVertex]:
            if x==endVertex:
                self.__out[startVertex].remove(x)
    '''isEdge function, input data: start and end, 2 vertices, returns 1 if there is an edge, 0 otherwise'''
    def isEdge(self,start,end):
        ok=0
        for i in self.__in[end]:
            if i==start:
                ok=1
        return ok
    '''input data: a vertex, returns the in degree of a vertex'''
    def inDegree(self,vertex):
        if vertex in self.__in.keys():
            return len(self.__in[vertex])
        return 0
    '''input data: a vertex, returns the out degree of a vertex'''
    def outDegree(self,vertex):
        if vertex in self.__out.keys():
            return len(self.__out[vertex])
        return 0
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
