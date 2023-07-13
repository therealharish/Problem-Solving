class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        degree = [0] * len(graph)

        map = {i:[] for i in range(len(graph))}

        for i in range(len(graph)):
            for j in graph[i]:
                map[j].append(i)
                degree[i] += 1
        
        ans = set()
        q  = deque()
        for i in range(len(degree)):
            if degree[i] == 0:
                ans.add(i)
                q.append(i)
        while(q):
            node = q.popleft()
            for i in map[node]:
                degree[i] -= 1
                if degree[i] == 0:
                    q.append(i)
                    ans.add(i)
        
        return sorted(ans)