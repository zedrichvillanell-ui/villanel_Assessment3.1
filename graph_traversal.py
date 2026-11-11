from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, bidirectional=True):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        if bidirectional:
            self.adj[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        traversal = []

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    def dfs(self, start_node):
        visited = set()
        traversal = []

        def _dfs(node):
            visited.add(node)
            traversal.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    _dfs(neighbor)  # Fixed: passes neighbor instead of node

        _dfs(start_node)
        return traversal

if __name__ == "__main__":
    g = Graph()
    # Edges based on diagram 2
    g.add_edge('V', 'I')
    g.add_edge('V', 'L')
    g.add_edge('I', 'L')
    g.add_edge('I', 'A')
    g.add_edge('L', 'N')
    g.add_edge('A', 'N')
    g.add_edge('A', 'L_bottom')
    g.add_edge('N', 'E')
    g.add_edge('E', 'L_bottom')

    print("Graph BFS Traversal:", " -> ".join(g.bfs('V')))
    print("Graph DFS Traversal:", " -> ".join(g.dfs('V')))