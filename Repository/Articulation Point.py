edges = [[1, 2], [2, 0], [0, 3], [3, 4], [1, 0]]
n = 5
edges = [[1, 2], [2, 3], [3, 1], [3, 4], [3, 6], [6, 7], [5, 7], [3,5]]
n = 8

# to find articulation point

graph = {i:[] for i in range(n)}
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
    
def solve(graph):
    visited = [False for i in range(n)]
    low = [0 for i in range(n)]
    disc = [0 for i in range(n)]
    time = 0
    
    def dfs(node, parent, time):
        nonlocal visited, low, disc
        visited[node] = True
        low[node] = disc[node] = time
        time += 1
        for child in graph[node]:
            if not visited[child]:
                dfs(child, node, time)
                low[node] = min(low[node], low[child])
                if low[child] > disc[node]:
                    print(node, child)
            elif child != parent:
                low[node] = min(low[node], disc[child])
    
    dfs(0, -1, time)
    
solve(graph)

        