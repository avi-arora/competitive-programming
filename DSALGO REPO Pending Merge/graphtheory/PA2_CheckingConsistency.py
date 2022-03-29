from GraphAdjList import Graph, Vertex


def HasCycleUsingDFSModification(G: Graph):
    """
    Returns 1 if graph G contains a cycle else returns 0
    TimeComplexity:
    SpaceComplexity:
    """
    pass

def HasCycleUsingLinearTopologicalSort(G: Graph):
    """
    Returns 1 if graph contains cycles else returns 0
    uses DFS graph traversal technique
    Uses the following theorem to check if graph has cycle or not
    Theorem: A DAG always has at-least one source and one sink
    Algorithm: 
    s1: find a source 
    s2: delete the newly searched source 
    s3: find another source and repeat from step 2
    s4: after end if DAG then G will be empty else a cycle exist.
    TimeComplexity: O(V+E)
    SpaceComplexity: O(V)
    """
    # uses linear topological ordering
    # apply linear topological order in subrouting

    sorted, queue = [], []

    # add all the zero degree element in queue
    for vertex in G.getVertices():
         if G.getInDegree(vertex) == 0:
             queue.append(vertex)

     # apply repeated InDegree computation
    while queue:
        zeroDegreeLabel = queue.pop(0)
        sorted.append(zeroDegreeLabel)
        # remove vertex from graph
        G.removeVertex(zeroDegreeLabel)
        # compute InDegree Computation again
        # vertex not in queue condition is important in algorithm
        # without this algorithm is very much ambiguous
        for vertex in G.getVertices():
            if G.getInDegree(vertex) == 0 and vertex not in queue:
                queue.append(vertex)
    
    #check if the graph contains vertices than the graph must contains cycle
    if G.getVertices() != 0:
        return 1
    else:
        return 0


def main():
    # take user input
    totalVertices, totalEdges = map(int, input().split(" "))
    G = Graph()

    # populate vertices
    for vertex in range(1, totalVertices+1):
        G.addVertex(vertex)

    # populate edges
    for _ in range(totalEdges):
        fromLabel, toLabel = map(int, input().split(" "))
        G.addEdge(fromLabel, toLabel, True)

    print(HasCycleUsingLinearTopologicalSort(G))


if __name__ == "__main__":
    main()
