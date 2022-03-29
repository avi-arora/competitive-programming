class Vertex:
    #constructor
    def __init__(self, label):
        """ 
        In this implementation weight/distance is only +ve
        for -ve weights, set weight=sys.MaxInt as initial value
        Note: weight should be consider +ve as of now 

        """
        self.label, self.visited = label, False
        self.neighbors, self.distance = {}, -1
        self.previous = None

    def __str__(self):
        return "VertexXX"

    def __repr__(self):
        return self.getVertexLabel() + "(" + str(id(self)) + ")"
    
    def getVertexLabel(self):
        return self.label

    def getDistance(self):
        return self.distance
    def setDistance(self, distance):
        self.distance = distance

    def setPrevious(self, label):
        self.previous = label

    def getPrevious(self):
        return self.previous

    def getConnections(self):
        return self.neighbors
    
    def isVisited(self):
        return self.visited
    
    def visit(self):
        self.visited = True
    
    def addNeighbor(self, neighbor,weight=0):
        """     
        Note: we don't need to do 'neighbor already exist validation' why?
        ans: because it's already saved in a dictionary
        """
        self.neighbors[neighbor] = weight
    
class Graph:
    def __init__(self):
        self.graph = {}

    #to make graph obj scriptable 
    def __getitem__(self, label):
        return self.graph[label]

    def __str__(self):
        return "GraphNODE"
    def __repr__(self):
        return "NDE"

    def getVertices(self):
        return self.graph.keys()
    
    def addVertex(self, label):
        self.graph[label] = Vertex(label)
    
    def totalVertices(self):
        return len(self.graph.keys())

    def addEdge(self, fromLabel, toLabel, weight=0,isDirected=False):
        """ This method also consider the edge cases
            if fromLabel and toLabel isn't a vertex yet, 
            it'll add them to vertex list
        """
        if fromLabel not in self.getVertices():
            self.addVertex(fromLabel)
        if toLabel not in self.getVertices():
            self.addVertex(toLabel)
        self.graph[fromLabel].addNeighbor(toLabel,weight)
        if not isDirected:
            self.graph[toLabel].addNeighbor(fromLabel,weight)
    
    def getEdges(self):
        edges = []
        for v in self.getVertices():
            edgePairs = []
            for e in self.graph[v].getConnections():
                edgePairs.append([v,e])
            edges.append(edgePairs)
        return edges

    def printGraph(self):
        for v in self.getVertices():
            print(f"{v}, Dist:", end=" ")
            print(self.graph[v].getDistance())
            print(self.graph[v].getConnections())        

#driver program
if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addEdge('a','b',10)
    G.addEdge('a','c',10)
    G.printGraph()
    print(G.getEdges())


    