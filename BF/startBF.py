def citire():
    global n
    n=int(input("Nr vertices: "))
    m=int(input("Nr edges: "))
    inbound={}
    for i in range (0,n):
        inbound[i]=[]
    for i in range (0,m):
        x=int(input())
        y=int(input())
        inbound[y].append(x)
    return inbound
def bf(start,end,inbound):
    c=[]
    viz=[]
    d=[]
    for i in range (0,n):
        viz.append(0)
        d.append(9999999)
    c.append(end)
    viz[end]=1
    d[end]=0
    while c != []:
        vertex=c[0]
        c.pop(0)
        for i in inbound[vertex]:
            if viz[i]==0:
                viz[i]=1
                c.append(i)
                d[i]=d[vertex]+1

    if d[start]==9999999:
        print("There is no path!")
    else:
        print("Distance is ",d[start])

def start():
    inbound=citire()
    start=int(input("Input start vertex: "))
    end=int(input("Input end vertex: "))
    bf(start,end,inbound)
start()
