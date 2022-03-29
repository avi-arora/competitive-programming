from GraphAdjList import Graph, Vertex


def AddingExitToMaze(G: Graph):
    """
    This returns the total number of connected component in a graph
    TimeComplexity: 
    SpaceComplexity: 
    """
    def Util(V: Vertex):
        V.visit()
        for nbr in V.getConnections():
            if not G[nbr].isVisited():
                Util(G[nbr])

    connectedComponent = 0
    for v in G.getVertices():
        if not G[v].isVisited():
            #visit recursive using utility
            Util(G[v])
            connectedComponent += 1
    
    return connectedComponent



if __name__ == '__main__':
    #take input
    totalVertices, totalEdges = input().split(" ")
    G = Graph() 
    for _ in range(int(totalEdges)):
        u, v = input().split(" ")
        G.addEdge(u,v)
    print(G.getVertices())
    #compute and print
    print(AddingExitToMaze(G))
