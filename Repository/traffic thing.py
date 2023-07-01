from typing import List
from collections import deque

def fightingTraffic(n: int, m: int, roads: List[List[int]], t: List[int], f: List[int], x: int) -> int:
    low = 0  # Minimum traffic tolerance
    high = int(1e9)  # Maximum traffic tolerance
    result = -1
    
    def getanswerthatistotalFun(n: int, m: int, graph: List[List[int]], f: List[int], tolerance: int) -> int:
        visited = [0] * n
        totalFun = 0
        q = deque()
        q.append(0)
        visited[0] = 1

        while q:
            city = q.popleft()
            totalFun |= f[city]

            for neighbor in graph[city]:
                if visited[neighbor] == 0 and tolerance >= 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

        return totalFun

    while low <= high:
        mid = low + (high - low) // 2
        graph = [[] for _ in range(n)]

        for i in range(m):
            city1 = roads[i][0]
            city2 = roads[i][1]
            traffic = t[i]

            if traffic <= mid:
                graph[city1].append(city2)
                graph[city2].append(city1)

        totalFun = getanswerthatistotalFun(n, m, graph, f, mid)
        if totalFun >= x:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
