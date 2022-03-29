from GraphAdjList import Graph, Vertex


def FindingExitFromMaze(G: Graph, U: Vertex, V):
    """
    G: Simple Undirected Graph
    U & V: Source and destination vertex
    Check if there exits a valid path between u & v
    TimeComplexity:
    SpaceComplexity:

    """
    def Util(vertex: Vertex):
        #base case
        if vertex.getLabel() == V:
            vertex.visit()
            return 1
        if not vertex.isVisited():
            vertex.visit()
            for nbr in vertex.getConnections():
                if not G[nbr].isVisited():
                    return Util(G[nbr])
        return 0

    return Util(U)
    

if __name__ == '__main__':
    #prepare input
    totalVertices, totalEdges = input().split(" ")
    G = Graph()

    for _ in range(int(totalEdges)):
        u, v = input().split(" ")
        G.addEdge(u,v)

    source, destination = input().split(" ")
    #compute and gives back result
    print(FindingExitFromMaze(G,G[source], destination))

