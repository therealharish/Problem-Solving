from collections import deque

t = int(input())

while t > 0:
    n, m, k = map(int, input().split())
    
    g = [[] for _ in range(n + 1)]
    mail = list(map(int, input().split()))
    
    dist = list(map(int, input().split()))
    
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
        
    q = deque()
    v = [0] * (n + 1)
    
    for i in range(k):
        q.append([mail[i], 1, dist[i]])
        v[mail[i]] = 1
    
    while q:
        cur = q.popleft()
        for x in g[cur[0]]:
            d = cur[1] + 1
            if v[x] or d > cur[2]:
                continue
            q.append([x, d, cur[2]])
            v[x] = 1
    
    res = "YES\n" if all(v[1:]) else "NO\n"
    print(res)
    
    t -= 1
