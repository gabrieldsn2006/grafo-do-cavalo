from collections import deque


class BreadthFirstPaths:

    def __init__(self, graph, source):
        self.source = source
        self.visited = [False] * graph.V
        self.edge_to = [-1] * graph.V
        self.order = []
        self._bfs(graph, source)

    def _bfs(self, graph, source):
        queue = deque()
        self.visited[source] = True
        queue.append(source)

        while queue:
            v = queue.popleft()
            self.order.append(v)
            for w in reversed(list(graph.adj[v])):  # inverte para respeitar ordem de inserção
                if not self.visited[w]:
                    self.visited[w] = True
                    self.edge_to[w] = v
                    queue.append(w)

    def has_path_to(self, v):
        return self.visited[v]

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