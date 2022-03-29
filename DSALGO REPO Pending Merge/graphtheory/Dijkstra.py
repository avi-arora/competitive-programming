from GraphAdjListWithWeights import Graph, Vertex
import heapq


def Dijkstra(G: Graph, Src: Vertex):
    #step 1 - set the distance of all the vertices to infinity
    for vertex in G.getVertices():
        G[vertex].setDistance(float("inf"))
    
    #step 2 - set distance of src vertex to 0
    Src.setDistance(0)

    #step 3 - build min heap
    unvisited_vertices = [(G[v].getDistance(), v) for v in G.getVertices()]
    heapq.heapify(unvisited_vertices)
    #unvisited_vertices = []
    #for v in G.getVertices():
    #   heapq.heappush(unvisited_vertices, (G[v].getDistance(), v))

    while unvisited_vertices:
        vertex = heapq.heappop(unvisited_vertices)[1]
        G[vertex].visit()
        for nbr, distance in G[vertex].getConnections().items():
            if not G[nbr].isVisited():
                if G[vertex].getDistance() + distance < G[nbr].getDistance():
                    #update the distance 
                    G[nbr].setDistance(G[vertex].getDistance() + distance)
                    G[nbr].setPrevious(G[vertex].getVertexLabel())

                    #update the heap by popping all the elements and re-insert it. 
                    while unvisited_vertices:
                        heapq.heappop(unvisited_vertices)
                    
                    unvisited_vertices = [(G[v].getDistance(), v) for v in G.getVertices() if not G[v].isVisited()]
                    heapq.heapify(unvisited_vertices)

if __name__ == "__main__":
    g = Graph()
    g.addEdge('A', 'B', 4, True)
    g.addEdge('A', 'C', 1, True)
    g.addEdge('B', 'E', 4, True)
    g.addEdge('C', 'B', 2, True)
    g.addEdge('C', 'D', 4, True)
    g.addEdge('D', 'E', 4, True)

    g.printGraph()
    Dijkstra(g,g['A'])
    g.printGraph()

    







