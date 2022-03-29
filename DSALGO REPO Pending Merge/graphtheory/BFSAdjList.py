from GraphAdjList import Graph, Vertex

def BFSWithoutDistance(G: Graph):
    """
    Returns a list of vertices (labels) traversed in BFS order
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    visited, queue = [], []
    queue.append(G.getVertex(list(G.getVertices())[0]))
    while queue:
        elem = queue.pop(0)
        if not elem.isVisited():
            elem.visit()
            visited.append(elem.getLabel())
            for nbr in elem.getConnections():
                if not G[nbr].isVisited():
                    queue.append(G[nbr])

    return visited

def BFSWithDistance(G: Graph, srcVertex: Vertex):
    """
    Returns a list of vertices (labels) traverse in BFS Order
    Also computes the distance between the source vertices to the other vertices
    TimeComplexity: O(V+E)
    SpaceComplexity: ??
    """
    queue, visited = [], []
    srcVertex.distance = 0
    queue.append(srcVertex)

    while queue:
        v = queue.pop(0)
        if not v.isVisited():
            #very common mistake to use v.visit instead of g[v].visit, 
            #while putting data into queue, it copy not set reference. 
            G[v.getLabel()].visit()
            visited.append(v.getLabel())
            for nbr in v.getConnections():
                if not G[nbr].isVisited():
                    queue.append(G[nbr])
                    G[nbr].setDistance(v.getDistance() + 1)
    
    return visited



def sampleGraph():
    G = Graph()
    G.addVertex("A")
    G.addVertex("B")
    G.addVertex("C")
    G.addVertex("D")
    G.addVertex("E")
    G.addVertex("F")
    G.addVertex("G")
    G.addVertex("H") 

    G.addEdge("A","B")
    G.addEdge("B","H")
    G.addEdge("B","C")
    G.addEdge("C","E")
    G.addEdge("C","D")
    G.addEdge("E","G")
    G.addEdge("E","F")
    G.addEdge("E","H")

    return G


if __name__ == "__main__":
    print(BFSWithDistance(sampleGraph(),sampleGraph().getVertex('A')))
    
