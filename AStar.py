import heapq

def add_edge(graph, u, v, cost):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, cost))
    graph[v].append((u, cost))


def a_star(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        
        if current == goal:
            break
        
        for neighbor, cost in graph[current]:
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct the path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def heuristic(node, goal):
    # Simple heuristic: absolute difference
    return abs(node - goal)

# User input
graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    graph[i] = []

m = int(input("Enter number of edges: "))
for _ in range(m):
    u, v, cost = map(int, input("Enter edge (u v cost): ").split())
    add_edge(graph, u, v, cost)

start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

# A* Algorithm
path = a_star(graph, start_node, goal_node, heuristic)
print("A* Path:", path)

"""
Enter number of vertices: 4
Enter number of edges: 5
Enter edge (u v cost): 1 2 5
Enter edge (u v cost): 1 3 10
Enter edge (u v cost): 2 4 2
Enter edge (u v cost): 3 4 1
Enter edge (u v cost): 4 5 7
Enter the start node: 1
Enter the goal node: 4
A* Path: [1, 2, 4]
"""
