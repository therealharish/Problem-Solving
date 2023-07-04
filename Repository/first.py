n, k = map(int, input().split())
edges = []
for i in range(n):
    edges.append(list(map(int, input().split())))
    
adj = {i:[] for i in range(1000)}
for src, dst in edges:
    adj[src].append(dst)
    adj[dst].append(src)
    
count = 0
for i in adj:
    if len(adj[i]) >= k:
        count += 1
print(count)