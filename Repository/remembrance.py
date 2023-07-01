from typing import *
from collections import deque


def remembrance(m: int, n: int, conditions: List[List[int]]) -> int:
    
    for i in range(len(conditions)):
        conditions[i] = (conditions[i], i)
    conditions.sort(key = lambda x: x[0][0])
    completed = 0
    visited = set()
    needed = set()
    
    # print(conditions)
    q = deque()
    for condition in conditions:
        q.append(condition)
        
    if conditions[0][0][0] != 0:
        return 0
    
    while(q):
        condition = q.popleft()
        should = condition[0][0]
        x = condition[0][1:]
        num = condition[1]
        # print(visited, should, x, num)
        # print()
        if should > (completed/n)*100:
            flag = 0
            for i in range(len(q)):
                if q[i][0][0] < should:  
                    q.append(condition)
                    flag = 1
                    break
            if flag:
                continue
            else:
                return 0
        count = 0
        for i in x:
            if i == -1 or i in visited:
                count += 1
            if i == num:
                return 0
        if count == len(x):
            visited.add(num)
            completed += 1
        else:
            q.append(condition)
            
        
        
    if len(visited) == n:
        return 1
    else:
        return 0
    
t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    conditions = []
    for i in range(n):
        conditions.append(list(map(int, input().split())))
    print(remembrance(m, n, conditions))
        