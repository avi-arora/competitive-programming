class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False

    #member methods 
    def visited(self):
        self.visited = True
    
    def getVertex(self):
        return self.id
    
    def setVertex(self, id):
        self.id = id
    
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    

class Graph:
    def __init__(self, numOfVertices, cost=0):
        self.adjMatrix = [[-1] * numOfVertices for _ in range(numOfVertices)]
        self.totalVertices = numOfVertices
        self.vertices = []
        for v in range(0, numOfVertices):
            self.vertices.append(Vertex(v))
        
    #sets a vertex
    def setVertex(self, vtx, id):
        if 0 <= vtx < self.totalVertices:
            self.vertices[vtx].setVertex(id)
    
    #gets a vertex
    def getVertex(self, id):
        for v in range(0, self.totalVertices):
            if self.vertices[v].getVertex() == id:
                return v
        return -1

    def addEdge(self, frm, to, cost=0, isDirected=False):
        #find from position 
        fromPosition, toPosition = self.getVertex(frm), self.getVertex(to)
        if fromPosition != -1 and toPosition != -1:
            self.adjMatrix[fromPosition][toPosition] = cost
            if not isDirected:
                self.adjMatrix[toPosition][fromPosition] = cost

    def getVertices(self):
        vertices = []
        for v in range(self.totalVertices):
            vertices.append(self.vertices[v].getVertex())
        return vertices

    def printMatrix(self):
        for u in range(self.totalVertices):
            rows = []
            for v in range(self.totalVertices):
                rows.append(self.adjMatrix[u][v])
            print(rows)
    #get all the edges
    def getEdges(self):
        edges = []
        for u in range(self.totalVertices):
            for v in range(self.totalVertices):
                if self.adjMatrix[u][v] != -1:
                    edges.append((self.vertices[u].getVertex(), self.vertices[v].getVertex()))
        return edges

#run the program 
if __name__ == '__main__':
    G = Graph(5)
    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')

    G.addEdge('a','e')
    G.addEdge('a','c')
    G.addEdge('c','b')
    G.addEdge('b','e')
    G.addEdge('e','d')
    G.addEdge('f','e')
    G.printMatrix()
    print(G.getEdges)
                    

            



    