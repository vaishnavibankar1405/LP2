from collections import deque

def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Build graph from user input
graph = {}
m = int(input("Enter number of edges: "))
for _ in range(m):
    u, v = map(int, input("Enter edge (u v): ").split())
    add_edge(graph, u, v)

start_node = int(input("Enter starting node: "))
print("BFS Traversal:")
bfs(graph, start_node)
