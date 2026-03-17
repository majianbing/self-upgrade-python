from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, start_node):
    visited = set()
    # Initialize deque as a queue
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        # Pop from the LEFT (First-In, First-Out)
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("BFS Path:")
bfs(graph, 'A')