edges = [[1, 2], [1, 4], [2, 4], [2, 5], [3, 4], [4, 5]]
n = 5
# edges = [[1, 2], [1, 3], [2, 5], [3, 4], [4, 5]]
# n = 5



adj = {i:[] for i in range(1, n+1)}
for src, dst in edges:
    adj[src].append(dst)
    
dp = {}
def dfs(node, destination):
    if node in dp:
        return dp[node]
    if node == destination:
        return 0
    res = -float('inf')
    for nei in adj[node]:
        res = max(res, dfs(nei, destination))
    dp[node] = res+1
    return dp[node]


def solveTabulation(src, destination):
    dp = [0] * (n+1)
    dp[src] = 0
    for i in range(src+1, destination+1):
        for j in range(src, i):
            if [j, i] in edges:
                dp[i] = max(dp[j]+1, dp[i])
    print(dp)
    return dp[destination]
# print(dfs(1, 5))
print(solveTabulation(1, 5))