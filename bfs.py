from queue import Queue

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['D', 'A'],
    'C': ['A'],
    'D': ['A', 'B', 'E'],
    'E': ['D']
}

visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in graph.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1  # inf

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()
    bfs_traversal_output.append(u)

    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v)
print("BFS : ", bfs_traversal_output)

# shortest path
v = "D"
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)
