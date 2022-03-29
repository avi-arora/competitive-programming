from GraphAdjList import Graph, Vertex

def GetBipartiteSets(G: Graph, startingVertex: Vertex = None):
    """
    Returns list of list of two set of bipartite graph. 
    if not bipartite return empty listd
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    pass



def isBipartite(G: Graph, StartingVertex: Vertex = None):
    """
    Return 1 if graph is bipartite else return 0
    G: Undirected graph in adjacency list format.
    TimeComplexity: 
    SpaceComplexity: 
    """
    if StartingVertex is None:
        StartingVertex = G[list(G.getVertices())[0]]
    
    queue = []
    StartingVertex.setColor(True)
    queue.append(StartingVertex)

    while queue:
        vertex = queue.pop(0)
        if not vertex.isVisited():
            vertex.visit()
            for nbr in vertex.getConnections():
                if not G[nbr].isVisited():
                    queue.append(G[nbr])
                    if G[nbr].getColor() is None: 
                        G[nbr].setColor(not vertex.getColor())
                    elif G[nbr].getColor() == vertex.getColor(): 
                        return 0
        
    return 1
            


def main():
    totalVertices, totalEdges = map(int, input().split(" "))
    G = Graph()
    for v in range(totalVertices):
        G.addVertex(v+1)
    
    for _ in range(0, totalEdges):
        u, v = map(int, input().split(" "))
        G.addEdge(u, v, False)

    print(isBipartite(G))



if __name__ == "__main__":
    main()