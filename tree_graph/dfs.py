from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def dfs_iterative(graph, start_node):
    visited = set()
    # Initialize deque as a stack
    stack = deque([start_node])
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
print("Iterative DFS Path:")
dfs_iterative(graph, 'A')