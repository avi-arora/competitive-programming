from GraphAdjList import Graph, Vertex
import copy


def TopologicalSort(G: Graph):
    """
    This function will return list of label sorted in topological ordering. 
    Uses slight modification of DFS
    TimeComplexity: For Original Topological Sorting O(|v|^2) for optimized version: O(V + E)
    SpaceComplexity: 
    """
    sorted = []
    def Util(v: Vertex):
        v.visit()
        for nbr in v.getConnections():
            if not G[nbr].isVisited():
                Util(G[nbr])
        #sink of a graph.
        sorted.append(v.getLabel())
    
    for vertex in G.getVertices():
        if not G[vertex].isVisited():
            Util(G[vertex])
    
    return sorted[::-1]
        

def TopologicalSortLinear(G: Graph):
    """
    Returns topological sorted vertex list of graph G, 
    uses linear approach, relies upon queues and InDegree Computation approach. 
    TimeComplexity: O(V+E), same as recursive with backtracking one (efficient algorithm as well)
    SpaceComplexity: ?
    """
    #deep copy the original graph
    #not necessary needed in sample programs
    G = copy.deepcopy(G)
    sorted, queue = [], []

    #add zero-InDegree vertices in queue, initial step
    for vertex in G.getVertices():
        if G.getInDegree(vertex) == 0:
            #add in queue
            queue.append(vertex)
    
    #zero InDegree items in queue are starting point of algorithm. 
    #run the algorithm while queue is not empty
    while queue:
        zeroVertex = queue.pop(0)
        sorted.append(zeroVertex)
        #remove the zero vertex from the graph
        G.removeVertex(zeroVertex)
        #re-calculate the InDegree of vertex and enqueue the one with 0 InDegree
        #condition vertex not in queue is important without it algorithm is ambiguous
        for vertex in G.getVertices():
            if G.getInDegree(vertex) == 0 and vertex not in queue:
                queue.append(vertex)
        
    return sorted
 


def TopologicalSortBruteForce(G: Graph):
    """
    un-optimized version of topological sorting
    """
    pass

         

if __name__ == "__main__":
    G = Graph()
    #G.addVertex("A")
    #G.addVertex("B")
    #G.addVertex("C")
    #G.addVertex("D")
    #G.addVertex("E")

    #G.addEdge("A", "B", True)
    #G.addEdge("B", "C", True)
    #G.addEdge("C", "D", True)
    #G.addEdge("A", "E", True)
    
    G.addVertex("2")
    G.addVertex("3")
    G.addVertex("5")
    G.addVertex("7")
    G.addVertex("8")
    G.addVertex("9")
    G.addVertex("10")
    G.addVertex("11")

    G.addEdge("7","8",True)
    G.addEdge("7","11", True)
    G.addEdge("5","11", True)
    G.addEdge("3","8", True)
    G.addEdge("3","10", True)
    G.addEdge("11","9", True)
    G.addEdge("11","10", True)
    G.addEdge("8","9", True)
    G.addEdge("11","2", True)

    print(TopologicalSort(G)) 
    print(TopologicalSortLinear(G))