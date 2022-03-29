from GraphAdjList import Graph, Vertex


def DFSWithPreAndPostVisitMarkers(G: Graph):
    """
    This function computes pre and post visit of a graph using DFS algorithm 
    TimeComplexity: O(V+E)
    SpaceComplexity: O(1)
    """
    def DFSUtil(v: Vertex):
        nonlocal counter
        #visit the vertex 
        v.visit()
        #increment previsit
        counter += 1
        v.preVisit(counter)
        for nbr in v.getConnections():
            if not G[nbr].isVisited():
                DFSUtil(G[nbr])
        #increment postvisit
        counter += 1
        v.postVisit(counter)

    #variable to keeps track of pre and post visit
    counter = 0
    #iterate every vertex
    for vertex in G.getVertices():
        #if vertex is not visited, visit using DFS
        # this condition also avoid unnecessary util calls
        if not G[vertex].isVisited():
            DFSUtil(G[vertex])
        
    


def printPreAndPostVisit(G: Graph):
    for u in G.getVertices():
        print(f"Label: {u} PreVisit: {G[u].getPre()} PostVisit: {G[u].getPost()}")


if __name__ == "__main__":
    G = Graph()
    G.addVertex('1')
    G.addVertex('2')
    G.addVertex('3')
    G.addVertex('4')
    G.addVertex('5')
    G.addVertex('6')

    G.addEdge('1','2')
    G.addEdge('1','3')
    G.addEdge('2','4')
    G.addEdge('4','3')
    G.addEdge('3','5')
    G.addEdge('5','6')

    DFSWithPreAndPostVisitMarkers(G)
    printPreAndPostVisit(G)
    
    






    



