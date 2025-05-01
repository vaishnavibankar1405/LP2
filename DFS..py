def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Build graph from user input
graph = {}
m = int(input("Enter number of edges: "))
for _ in range(m):
    u, v = map(int, input("Enter edge (u v): ").split())
    add_edge(graph, u, v)

start_node = int(input("Enter starting node: "))
print("DFS Traversal:")
dfs(graph, start_node, set())
