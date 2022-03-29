from GraphAdjList import Graph, Vertex

def getSCCBruteForce(G: Graph):
    pass

def countSCCBruteForce(G: Graph):
    pass


def getSCC(G: Graph):
    """
    Returns a list of list of strongly connected components
    TimeComplexity: O(V+E) linear
    SpaceComplexity: 
    """
    pass

def countSCC(G: Graph):
    """
    Returns number of strongly connected component in a graph G
    TimeComplexity: O(V+E) Linear
    SpaceComplexity: ??
    """
    
    def exploreAndRemove(V: Vertex, verticesToRemove):
        if not V.isVisited():
            V.visit()
            for nbr in V.getConnections():
                if not G[nbr].isVisited():
                    exploreAndRemove(G[nbr],verticesToRemove)
                    verticesToRemove.append(nbr)

            verticesToRemove.append(V.getLabel())
            #remove all the visited vertices
            for v in verticesToRemove:
                G.removeVertex(v)
            return verticesToRemove

    #reverse a graph
    revG = G.transpose()
    #get vertices in reverse post visit in reverse graph
    revPostOrderVertices = [v.getLabel() for v in revG.reversePostVisit()]

    counter = 0
    while revPostOrderVertices:
        vertex = revPostOrderVertices.pop(0)
        if not G[vertex].isVisited():
            verticesToRemove = exploreAndRemove(G[vertex],[])
            counter += 1
            for v in verticesToRemove:
                if v in revPostOrderVertices:
                    revPostOrderVertices.remove(v)

    return counter


def main():
    totalVertex, totalEdges = map(int, input().split(" "))
    G = Graph()

    for v in range(1,totalVertex+1):
        G.addVertex(v)
    
    for _ in range(totalEdges):
        fromVertex, toVertex = map(int, input().split(" "))
        G.addEdge(fromVertex, toVertex,True)
    
    print(countSCC(G))



if __name__ == "__main__":
    main()