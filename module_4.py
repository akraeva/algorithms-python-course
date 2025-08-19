# Stepick.org — Алгоритмы в Python — просто, наглядно, с нуля!
# 4.  Алгоритмы на графах

import heapq

# 4.1 Представление графов и обходы (BFS, DFS)


def m_4_1_1():
    def find_path(graph, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for neighbor in graph[start]:
            if neighbor not in path:
                new_path = find_path(graph, neighbor, end, path)
                if new_path:
                    return new_path
        return None


def m_4_1_2():
    def has_cycle(graph):
        stack = set()

        def dfs(node):
            if node in stack:
                return True
            stack.add(node)
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            stack.remove(node)
            return False

        for node in graph:
            if dfs(node):
                return True
        return False

    # print(has_cycle({"A": ["B"], "B": ["C"], "C": ["A"]}) is True)


def m_4_1_3():
    def graph_to_edges(graph):
        edges = []
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                edges.append((node, neighbor))
        return edges

    # print(graph_to_edges({"A": ["B"], "B": ["C"], "C": []}) == [("A", "B"), ("B", "C")])


# 4.2 Поиск кратчайших путей (Дейкстра, Беллман-Форд)


def m_4_2_1():

    # import heapq

    def get_shortest_path(graph, start, end):
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        previous = {node: None for node in graph}
        queue = [(0, start)]

        while queue:
            curr_dist, curr_node = heapq.heappop(queue)
            if curr_node == end:
                break

            for neighbor, weight in graph[curr_node].items():
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = curr_node
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous[node]

        path.reverse()

        return path if path[0] == start else None


def m_4_2_2():
    def reachable(graph, start):
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, {}):
                    dfs(neighbor)

        dfs(start)
        return sorted(visited)


def m_4_2_3():
    # в задании напрямую не говорится, что граф взвешенный,
    # поэтому проще его решить BFS
    def shortest_cycle(graph, start):
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            for neighbor in graph.get(current, {}):
                if neighbor == start and len(path) > 1:
                    return path + [start]
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        return None


# 4.3 Остовные деревья (Прим, Краскал)
