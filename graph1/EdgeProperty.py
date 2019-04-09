class EdgeProperty():
    def __init__(self):
        self.__edges={}
    '''input data: an edge and its value, returns 1 if the edge could be added and -1 otherwise'''
    def addEdge(self,edge,cost):
        for x in self.__edges:
            if x==edge:
                return -1
        self.__edges[edge]=cost
        return 1
    '''input data: an edge of the graph, removes an edge'''
    def removeEdge(self,edge):
        self.__edges.pop(edge)
    '''input data: an edge, returns the cost of a given edge'''
    def retrieveCost(self,edge):
        return int(self.__edges[edge])
    '''input data: an edge and the new cost, sets the cost of this edge to the new one'''
    def modifyCost(self,edge,newcost):
        self.__edges[edge]=newcost
    '''returns the list of edges'''
    def getEdges(self):
        return self.__edges
