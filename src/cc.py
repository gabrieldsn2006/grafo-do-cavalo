"""
Connected Components

Identifica componentes conectadas em um grafo não-dirigido.
Uma componente conectada é um conjunto máximo de vértices onde
existe um caminho entre qualquer par de vértices.

Complexidade:
    - Inicialização: O(V + E) usando DFS
    - Consultas: O(1)
"""


class ConnectedComponents:
    """
    Encontra componentes conectadas em um grafo não-dirigido.
    
    Attributes:
        id: lista que armazena o id da componente de cada vértice
        visited: lista booleana de vértices visitados
        count: número total de componentes conectadas
    """

    def __init__(self, graph):
        self.id = [-1] * graph.V
        self.visited = [False] * graph.V
        self.count = 0
        
        # Encontra todas as componentes conectadas
        for v in range(graph.V):
            if not self.visited[v]:
                self._dfs(graph, v)
                self.count += 1

    def _dfs(self, graph, v):
        self.visited[v] = True
        self.id[v] = self.count
        
        for w in graph.adj[v]:
            if not self.visited[w]:
                self._dfs(graph, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def component_id(self, v):
        return self.id[v]

    def num_components(self):
        return self.count

    def component_vertices(self, component):
        if component < 0 or component >= self.count:
            return []
        return [v for v in range(len(self.id)) if self.id[v] == component]

    def get_all_components(self):
        components = {}
        for comp in range(self.count):
            components[comp] = self.component_vertices(comp)
        return components

    def __str__(self):
        """Representação em string das componentes conectadas."""
        s = f"Connected Components (total: {self.count})\n"
        for comp in range(self.count):
            vertices = self.component_vertices(comp)
            s += f"Component {comp}: {vertices}\n"
        return s
