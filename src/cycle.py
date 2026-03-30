"""Cycle detection for an undirected graph.

- Conta ciclos simples.
- Lista vértices de cada ciclo.
- Usa DFS com reconstrução de ciclo via pilha de recursão.
"""


class CycleDetector:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * graph.V
        self.edge_to = [-1] * graph.V
        self._cycle_set = set()  # conjunto de ciclos normalizados
        self._cycles = []        # ciclo em lista de vértices

        for v in range(graph.V):
            if not self.visited[v]:
                self._dfs(v, -1, [])

    def _normalize_cycle(self, cycle):
        # Recebe lista de vértices cíclicos com repetição do vértice inicial no fim
        if len(cycle) < 2:
            return None

        base = cycle[:-1]  # remove repetição final
        min_v = min(base)
        min_idx = base.index(min_v)

        # rotaciona para começar pelo vértice mínimo
        rotated = base[min_idx:] + base[:min_idx]
        rotated_rev = list(reversed(rotated))

        if rotated_rev < rotated:
            rotated = rotated_rev

        return tuple(rotated)

    def _dfs(self, v, parent, stack):
        self.visited[v] = True
        stack.append(v)

        for w in self.graph.adj[v]:
            if not self.visited[w]:
                self.edge_to[w] = v
                self._dfs(w, v, stack)
            elif w != parent and w in stack:
                # Encontrado ciclo; extraí-lo da pilha
                cycle = stack[stack.index(w):] + [w]
                normalized = self._normalize_cycle(cycle)
                if normalized is not None and normalized not in self._cycle_set:
                    self._cycle_set.add(normalized)
                    self._cycles.append(list(normalized) + [normalized[0]])

        stack.pop()

    def has_cycle(self):
        return len(self._cycles) > 0

    def num_cycles(self):
        return len(self._cycles)

    def cycles(self):
        return self._cycles

    def __str__(self):
        if not self.has_cycle():
            return "Não há ciclo no grafo."

        s = f"Ciclos detectados: {self.num_cycles()}\n"
        for i, cycle in enumerate(self._cycles):
            s += f"Ciclo {i}: {cycle}\n"
        return s
