from operations import *
from copy import deepcopy
class Ui():
    def mainmenu(self):
        menu="";
        menu += "Construct a minimal spanning tree using the Kruskal's algorithm.\n"
        print(menu)
    def readVertex(self,nr):
        vertex=int(input())
        while vertex not in range(nr):
            print("Invalid vertex! Input a correct vertex:")
            vertex=int(input())
        return vertex
def showGraph(graf):
    print("Inbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.inEdges(i))
    print("Outbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.outEdges(i))
def loadFromFile():
    f = open("graph4.txt", "r")
    line = f.readline().strip().split()
    nrV = int(line[0])
    nrE    = int(line[1])
    graph = Graph(nrV)
    for i in range(nrE):
        line = f.readline().strip().split()
        startVertex = int(line[0])
        endVertex   = int(line[1])
        cost = int(line[2])
        graph.addEdge(startVertex, endVertex, cost)
    return graph

def start():
    ui=Ui()
    graph=loadFromFile()
    nr=graph.getNrV()
    nrv=graph.getNrV()
    ui.mainmenu()
    res=[]
    res=graph.Kruskal()
    gr = Graph(nrv)
    for elem in res:
         gr.addEdge(elem[0], elem[1], elem[2])
    nod=res[0][0]
    source=nod
    rez=[]
    viz=[]
    graph.df(nod,viz,nod,rez)
    rez.append(source)
    s=graph.compute(rez)
    print("Cycle:")
    print(rez)
    print("Cost:")
    print(s)
start()
