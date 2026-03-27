class DepthFirstPaths:

    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.V
        self.edge_to = [-1] * graph.V
        self.order = []
        self._dfs(graph, source)

    def _dfs(self, graph, v):
        self.visited[v] = True
        self.order.append(v)
        for w in reversed(list(graph.adj[v])):  # inverte para respeitar ordem de inserção
            if not self.visited[w]:
                self.edge_to[w] = v
                self._dfs(graph, w)

    def has_path_to(self, v):
        return self.visited[v]

    def reachable(self):
        return [v for v, vis in enumerate(self.visited) if vis]

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        path = []
        current = v
        while current != self.source:
            path.append(current)
            current = self.edge_to[current]
        path.append(self.source)
        path.reverse()
        return path

    def visit_order_to(self, v):
        if not self.has_path_to(v):
            return None

        path = self.path_to(v)
        return [self.order.index(vertex) + 1 for vertex in path]