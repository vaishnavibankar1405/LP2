import sys

def dijkstra(graph, src, V):
    dist = [sys.maxsize] * V
    dist[src] = 0
    sptSet = [False] * V

    for _ in range(V):
        u = min((v for v in range(V) if not sptSet[v]), key=lambda v: dist[v], default=None)
        sptSet[u] = True

        for v in range(V):
            if graph[u][v] and not sptSet[v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t {dist[i]}")

# Driver code
if __name__ == "__main__":
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    
    dijkstra(graph, 0, 9)  # Run Dijkstra starting from vertex 0
