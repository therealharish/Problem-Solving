n = 5
edges = [[1, 2, -1], [1, 3, 4], [2, 3, 3], [2, 4, 2], [2, 5, 2], [4, 2, 1], [4, 3, 5], [5, 4, -3]]
d = [float('inf') for _ in range(n+1)]
d[1] = 0
for i in range(n-1):
    for u, v, w in edges:
        if d[v] > d[u] + w:
            d[v] = d[u] + w
print(d)