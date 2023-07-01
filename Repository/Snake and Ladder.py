from functools import cache
import sys

x1, y1, x2, y2 = map(int, input().split())
ladder1 = list(map(int, input().split()))
ladder2 = list(map(int, input().split()))
ladder3 = list(map(int, input().split()))
# print(x1, x2, y1, y2, ladder1, ladder2, ladder3)


visited = set()
def solve(x, y):
    print(x, y)
    if (x, y) in visited:
        return float('inf')
    
    visited.add((x, y))
    
    if x == x2 and y == y2:
        return 0
    
    if x < 0 or x > x1 or y < 0 or y > y2:
        return float('inf')
    
    ans = min(1+solve(x+1, y), 1+solve(x-1, y), 1+solve(x, y+1), 1+solve(x, y-1))
    l1, l2, l3 = float('inf'), float('inf'), float('inf')
    if x == ladder1[0] and y == ladder1[1]:
        l1 = 10+solve(ladder1[2], ladder1[3])
    if x == ladder2[0] and y == ladder2[1]:
        l2 = 10+solve(ladder2[2], ladder2[3])
    if x == ladder3[0] and y == ladder3[1]:
        l3 = 10+solve(ladder3[2], ladder3[3])
        
    return min(ans, l1, l2, l3)

print(solve(x1, y1))





    
    

    