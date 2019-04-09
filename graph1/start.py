from operations import *
from EdgeProperty import *
from copy import deepcopy
class Ui():
    def mainmenu(self):
        menu="";
        menu += "1.  Show the number of vertices.\n"
        menu += "2.  Check if there is an edge between two vertices.\n"
        menu += "3.  Show the in and out degree of a vertex.\n"
        menu += "4.  Outbound edges of a specified vertex.\n"
        menu += "5.  Inbound edges of a specified vertex.\n"
        menu += "6.  Retrieve the value attached to an edge.\n"
        menu += "7.  Modify the value attached to an edge.\n"
        menu += "Bonus:\n"
        menu += "8.  Add an edge.\n"
        menu += "9.  Remove an edge.\n"
        menu += "10. Add a vertex.\n"
        menu += "11. Remove a vertex.\n"
        menu += "12. Show the initial graph.\n"
        menu += "13. Show the initial value map.\n"
        menu += "14. Show graph.\n"
        menu += "15. Show the value map.\n"
        menu += "0.  Exit\n"
        print(menu)
    def readOption(self,ms):
        opt=input(ms)
        while opt not in ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'):
            print("Invalid opion!\n")
            opt=input(ms)
        return int(opt)
    def readVertex(self,nr):
        vertex=int(input())
        while vertex not in range(nr):
            print("Invalid vertex! Input a correct vertex:")
            vertex=int(input())
        return vertex
    def readInteger(self,ms):
        number=input(ms)
        while number.isdigit()==False:
            print("Must be integer! ")
            number=input(ms)
        return int(number)
def loadFromFile():
    f = open("graph1.txt", "r")
    line = f.readline().strip().split()
    nrV = int(line[0])
    nrE    = int(line[1])
    graph = Graph(nrV)
    for i in range(nrE):
        line = f.readline().strip().split()
        startVertex = int(line[0])
        endVertex   = int(line[1])
        try:
            value = int(line[2])
        except:
            value = line[2]
        graph.addEdge(startVertex, endVertex)
        EP.addEdge((startVertex,endVertex),value)
    return graph
def showGraph(graf):
    print("Inbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.inEdges(i))
    print("Outbound edges: ")
    for i in range(0,graf.getNrV()):
        print(i,graf.outEdges(i))
def showValueMap(edges_list):
        for x in edges_list.keys():
            print(x, edges_list[x])


def start():
    global EP
    EP=EdgeProperty()
    ui=Ui()
    graph=loadFromFile()
    edges_list=EP.getEdges()
    initial_graph=deepcopy(graph)
    initial_edges=deepcopy(edges_list)
    nr=graph.getNrV()

    while True:
        ui.mainmenu()
        opt=ui.readOption("Enter option: ")
        if (opt==1):
            print("The number of vertices is",nr)
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
            print("Enter vertex: ")
            vertex=ui.readVertex(nr)
            in_degree=graph.inDegree(vertex)
            out_degree=graph.outDegree(vertex)
            print("In degree=",in_degree,"Out degree=",out_degree)
        elif (opt==4):
            print("Enter vertex: ")
            vertex=ui.readVertex(nr)
            out_list=graph.outEdges(vertex)
            if len(out_list)>0:
                print("The outbound edges of",vertex,"are",out_list )
            else:
                print("There are no outbound edges!")
        elif (opt==5):
            print("Enter vertex: ")
            vertex=ui.readVertex(nr)
            in_list=graph.inEdges(vertex)
            if len(in_list)>0:
                print("The inbound edges of",vertex,"are",in_list )
            else:
                print("There are no inbound edges!")
        elif (opt==6):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            if graph.isEdge(start,end)==1:
                edge=(start,end)
                cost=EP.retrieveCost(edge)
                print("The cost attached to edge",edge,"is",cost)
            else:
                print("There is no edge between",start,"and",end)
        elif (opt==7):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            if graph.isEdge(start,end)==1:
                edge=(start,end)
                newcost=ui.readInteger("Enter cost: ")
                EP.modifyCost(edge,newcost)
            else:
                print("There is no edge between",start,"and",end)
        elif (opt==8):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            cost=ui.readInteger("Enter cost: ")
            rez=EP.addEdge((start,end),cost)
            graph.addEdge(start,end)
            if rez==-1:
                print("Edge alrealy exists!")
        elif (opt==9):
            print("Enter start vertex: ")
            start=ui.readVertex(nr)
            print("Enter end vertex: ")
            end=ui.readVertex(nr)
            if graph.isEdge(start,end)==1:
                EP.removeEdge((start,end))
                graph.removeEdge(start,end)
            else:
                 print("There is no edge between",start,"and",end)
        elif (opt==10):
            vertex=ui.readInteger("Enter new vertex: ")
            graph.addVertex(vertex)
            nr=graph.getNrV()
        elif (opt==11):
            vertex=ui.readInteger("Enter vertex to remove: ")
            list_remove=[]
            list_remove=graph.removeVertex(vertex)
            for x in list_remove:
                EP.removeEdge(x)
            nr=graph.getNrV()
        elif (opt==12):
            showGraph(initial_graph)
        elif (opt==13):
            showValueMap(initial_edges)
        elif (opt==14):
            showGraph(graph)
        elif (opt==15):
            edges_list=EP.getEdges()
            showValueMap(edges_list)
        else:
            print("Exit.")
            break
start()
