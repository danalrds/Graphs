from operations import *
from copy import deepcopy
class Ui():
    def mainmenu(self):
        menu="";
        menu += "1. Compute the lowest length path.\n"
        menu += "2. Check if there is an edge between two vertices.\n"
        menu += "3. Show graph.\n"
        menu += "Bonus:\n"
        menu += "4. Find the strongly connected components.\n"
        menu += "5. Find the biconnected components of an undirected graph.\n"
        menu += "0.  Exit\n"
        print(menu)
    def readOption(self,ms):
        opt=input(ms)
        while opt not in ('0','1','2','3','4','5','6'):
            print("Invalid opion!\n")
            opt=input(ms)
        return int(opt)
    def readVertex(self,nr):
        vertex=int(input())
        while vertex not in range(nr):
            print("Invalid vertex! Input a correct vertex:")
            vertex=int(input())
        return vertex

def loadFromFile():
    f = open("graph2.txt", "r")
    line = f.readline().strip().split()
    nrV = int(line[0])
    nrE    = int(line[1])
    graph = Graph(nrV)
    for i in range(nrE):
        line = f.readline().strip().split()
        startVertex = int(line[0])
        endVertex   = int(line[1])
        graph.addEdge(startVertex, endVertex)
    return graph
def showGraph(graf):
    print("Inbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.inEdges(i))
    print("Outbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.outEdges(i))

def start():
    ui=Ui()
    graph=loadFromFile()
    initial_graph=deepcopy(graph)
    nr=graph.getNrV()
    global nrC
    nrC=1
    while True:
        ui.mainmenu()
        opt=ui.readOption("Enter option: ")
        if (opt==1):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            distance=graph.bf(start,end)
            if distance==None:
                 print("There is no path!")
            else:
                print("Distance is ",distance)
        elif (opt==2):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            if graph.isEdge(start,end)==1:
                print("There is an edge between",start,"and",end,"\n")
            elif graph.isEdge(start,end)==0:
                print("There is no edge between",start,"and",end,"\n")
        elif (opt==3):
            showGraph(graph)
        elif (opt==4):
            graph.compConex()
        elif (opt==5):
            graph.BCC()
            print ("Above are %d biconnected components in the graph" %(graph.count));
            print("")
        elif (opt==6):
            viz=[]
            start=int(input())
            viz=graph.df(start,viz);
            print(viz)
        else:
            print("Exit.")
            break
start()
