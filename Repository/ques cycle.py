n = int(input())
arr = list(map(int, input().split()))

adj = {i:[] for i in range(1, n+1)}
for i in range(1, n+1):
    adj[arr[i-1]].append(i)
# print(adj)

def detectCycle(adj):
    visited = [False] * (len(adj)+1)
    
    def dfs(i):
        print(visited)
        if visited[i]:
            return True
        visited[i] = True
        for j in adj[i]:
            if dfs(j):
                return True
        return False
    for i in range(1, len(adj)+1):
        if not visited[i]:
            if dfs(i):
                return True
    return False

if detectCycle(adj):
    print(0)
else:
    print(1)


# def detectCycle(adj):
    
    