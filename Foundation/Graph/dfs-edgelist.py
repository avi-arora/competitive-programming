
#dfs using edgelist


def dfs(edges):
    adjlist = {}
    for edge in edges:
        ui, vi = edge
        if ui not in adjlist:
            adjlist[ui] = [vi]
        else:
            adjlist[ui].append(vi)
        
        if vi not in adjlist:
            adjlist[vi] = [ui]
        else:
            adjlist[vi].append(ui)
    
    def dfs_helper(source,adjlist, visited):
        if source in visited:
            return 
        
        print(source)
        visited.append(source)

        for nbr in adjlist[source]:
            if nbr not in visited:
                dfs_helper(nbr, adjlist, visited)

    visited = []
    for node in adjlist.keys():
        dfs_helper(node, adjlist, visited)


if __name__ == "__main__":
    edges = [
        [0,2],
        [0,1],
        [1,2],
        [3, 4]
    ]

    dfs(edges)