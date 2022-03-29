"""

This file contains various combination of DFS (depth search algorithm)
with sources and time complexity.

"""
from GraphAdjList import *

def DFSAdjList(G: Graph):
    """
    Computes and return list of labels while traversing graph using DFS
    TimeComplexity: O(V + E) : why? give proof
    SpaceComplexity: O(V) - total vertex returned in DFS traversal order
    """
    #utility for recursive computation of path
    def DFSUtility(vertex : Vertex, path):
        """
        Takes a Vertex, Recursive traverse it's neighbors
        """
        if not vertex.isVisited():
            vertex.visit()
            path.append(vertex.getLabel())
        for neighbor in vertex.getConnections():
            if not G[neighbor].isVisited():
                DFSUtility(G[neighbor],path)
    #list to store label in traversal order
    dfsPath = []
    for vertex in G.getVertices():
        DFSUtility(G[vertex], dfsPath)

    return dfsPath

def DFSWithoutVisitedTracking(G: Graph):
    """
    This will implement DFS without considers visited ADT in DS. 
    In this we just ignore visited property in Graph, and assume we don't store that property
    TimeComplexity: O(V+E)
    SpaceComplexity: O(V) - Total vertex returned in DFS traversal order
    """
    def DFSUtility(vertex: Vertex):
        visited.append(vertex.getLabel())
        for nbr in vertex.getConnections():
            if nbr not in visited:
                DFSUtility(G.graph[nbr])
        

    visited = []
    for vertex in G.getVertices():
        #checking this condition here so to save calls to DFSUtility.
        if vertex not in visited:
            DFSUtility(G.graph[vertex])
    return visited
        

        



if __name__ == '__main__':
    print(DFSAdjList(SampleGraph_1()))
    print(DFSWithoutVisitedTracking(SampleGraph_1()))