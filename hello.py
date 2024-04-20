class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        print("parent : ",self.parent)
        print("rank   : ", self.rank)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            print(f"Rejected : u={u},root_u={root_u},v={v},root_v={root_v}")
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        print(f"Accepted : u={u},root_u={root_u},v={v},root_v={root_v}")
        return True

def sort_by_weight(edge):
    return edge[2]

def kruskal(graph):
    n = len(graph)
    graph.sort(key=sort_by_weight)  # Sort edges by weight
    mst = []
    ds = DisjointSet(n)

    for edge in graph:
        u, v, weight = edge
        if ds.union(u, v):
            mst.append(edge)
            print(" mst = ",mst)
        else:
            print("Rejected = ",edge)

    return mst

# Example usage:
graph = [
    (0, 1, 5), (0, 2, 1), (0, 3, 3),
    (1, 2, 3), (1, 3, 4), (2, 3, 2)
]
mst = kruskal(graph)
print("Minimum Spanning Tree (MST):", mst)
