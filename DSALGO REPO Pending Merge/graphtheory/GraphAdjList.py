import copy

class Vertex:
    def __init__(self, label):
        self.label, self.visited = label, False
        self.neighbors = []
        self.pre, self.post = 0, 0
        self.distance = float("-inf")
        #used to compute shortest path tree or BFS Tree
        self.parent = None
        self.color = None

    def addNeighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def removeNeighbor(self, nbr):
        """removes a neighbor from the vertex"""
        deletedNbr = None
        if nbr in self.neighbors:
            deletedNbr = self.neighbors.remove(nbr)
        return deletedNbr

    def getConnections(self):
        return self.neighbors

    def getVertexLabel(self):
        return self.label

    def visit(self):
        self.visited = True

    def preVisit(self, value):
        self.pre = value

    def postVisit(self, value):
        self.post = value

    def getPre(self):
        return self.pre

    def getPost(self):
        return self.post

    def isVisited(self):
        return self.visited

    def getLabel(self):
        return self.label
    
    def setDistance(self, dist):
        self.distance = dist
    
    def getDistance(self):
        return self.distance
    
    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color
    
    def getParent(self):
        return self.parent
    
    def setParent(self, label):
        self.parent = label
    


class Graph:
    def __init__(self):
        self.graph = {}

    def __getitem__(self, label):
        return self.graph[label]

    def totalVertices(self):
        return len(self.graph.keys())

    def addVertex(self, label):
        self.graph[label] = Vertex(label)

    def removeVertex(self, label):
        if label in self.graph:
            # delete from main graph
            self.graph.pop(label)

            # delete all neighbors
            for _, vertex in self.graph.items():
                vertex.removeNeighbor(label)

    def getVertices(self):
        return self.graph.keys()

    def getVertex(self, label):
        return self.graph[label]

    def getOutDegree(self, label):
        """
        returns the outdegree of a vertex
        works only with Directed Edges, useless in other edges
        """
        return len(self.graph[label].getConnections())

    def getInDegree(self, label):
        """
        returns the InDegree of a vertex, 
        works only with directed edges, useless in undirected graphs.
        also considers loops in vertex
        """
        inDegree = 0
        for vertex in self.graph:
            if label in self.graph[vertex].getConnections():
                inDegree += 1
        return inDegree

    def addEdge(self, fromLabel, toLabel, isDirected=False):
        """ This method also consider the edge cases
            if fromLabel and toLabel isn't a vertex yet, 
            it'll add them to vertex list
        """
        # handle corner cases listed in description
        if fromLabel not in self.getVertices():
            self.addVertex(fromLabel)
        if toLabel not in self.getVertices():
            self.addVertex(toLabel)
        # add the edge
        self.graph[fromLabel].addNeighbor(toLabel)
        # handle undirected graph case
        if not isDirected:
            self.graph[toLabel].addNeighbor(fromLabel)
    
    def removeEdge(self, fromLabel, toLabel, isDirected=False):
        if fromLabel in self.getVertices() and toLabel in self.getVertices():
            self.graph[fromLabel].removeNeighbor(toLabel)
            if not isDirected:
                self.graph[toLabel].removeNeighbor(fromLabel)

    def getEdges(self):
        edges = []
        for u in self.getVertices():
            individual = []
            for e in self.graph[u].getConnections():
                individual.append([u, e])
            edges.append(individual)
        return edges


    def transpose(self):
        """
        Returns a transpose (reverse) graph
        TimeComplexity: O(V+E)
        SpaceComplexity:
        """
        #makes a copy of graph
        G = Graph()
        for label, vertex in self.graph.items():
            for v in vertex.getConnections():
                G.addEdge(v,label,True)
        return G

    def Reverse(self):
        """
        Modifies the current graph and transpose (reverse) it. 
        TimeComplexity: 
        SpaceComplexity:
        """
        pass

    def computePreAndPostVisit(self):
        """
        Compute the Pre and Post visit of the graph.
        Uses DFS 
        Time Complexity: O(V+E)
        Space Complexity: O(1)
        """
        counter = 0
        def explore(V: Vertex):
            if not V.isVisited():
                V.preVisit(counter)
                V.visit()
                for nbr in V.getConnections():
                    if not G[nbr].isVisited():
                        explore(G[nbr])
                V.postVisit(counter)

        for vertex in self.graph:
            if not G[vertex].isVisited():
                explore(G[vertex])

    def postVisit(self):
        """
        Returns a list of label sorted in assending order or their post visit numbers 
        TimeComplexity: 
        SpaceComplexity:
        """
        pass

    def reversePostVisit(self):
        """
        Returns a list of labels sorted in decreasing order of their post visit numbers 
        TimeComplexity: 
        SpaceComplexity:
        Note: uses copy of graph G. as we don't want visit of original graph to be tampered.
        alternative approach would be to use visited list instead of object level storage for visit
        """
        G = copy.deepcopy(self)
        postVisits = []

        def explore(V: Vertex):
            if not V.isVisited():
                V.visit()
                for nbr in V.getConnections():
                    if not G[nbr].isVisited():
                        explore(G[nbr])
                postVisits.append(V)
        for vertex in G.getVertices():
            if not G[vertex].isVisited():
                explore(G[vertex])

        return postVisits[::-1]




    def printGraph(self):
        print("<<Graph>> ")
        for label, vertex in self.graph.items():
            print(f"Vertex: {label} Connections: {vertex.getConnections()}")

    def visualize(self):
        """
        Print a Visualization of a graph
        """
        pass



def SampleGraph_1():
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')

    G.addEdge('a', 'b')
    G.addEdge('b', 'c')
    G.addEdge('c', 'd')
    G.addEdge('c', 'e')
    G.addEdge('f', 'e')
    G.addEdge('e', 'g')
    G.addEdge('e', 'h')
    G.addEdge('b', 'h')

    return G


if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addEdge('a', 'b', True)
    G.addEdge('a', 'c', True)
    S = G.transpose()
    G.printGraph()
    S.printGraph()
