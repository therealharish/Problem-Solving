#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

# tle
def componentsInGraph1(gb):
    
    m = float('-inf')
    for i, j in gb:
        m = max(m, i, j)

    rep = [i for i in range(m+1)]
    
    def union(i, j):
        r1 = find(i)
        r2 = find(j)
        for k in range(len(rep)):
            if rep[k] == r2:
                rep[k] = r1
    
    def find(i):
        return rep[i]
                
    
    for i in range(len(gb)):
        a, b = gb[i]
        union(a, b)
        
    d = Counter(rep[1:])
    ans = [float('inf'), float('-inf')]
    for i in d:
        if d[i] >= 2:
            ans[0] = min(ans[0], d[i])
            ans[1] = max(ans[1], d[i])
    return ans

# path compression
def componentsInGraph(gb):
    
    m = float('-inf')
    for i, j in gb:
        m = max(m, i, j)

    rep = [i for i in range(m+1)]
    
    def union(a, b):
        r1 = find(a)
        r2 = find(b)
        if r1!=r2:
            rep[r2] = r1

    def find(a):
        if rep[a] == a:
            return a
        else:
            rep[a] = find(rep[a])
            return rep[a]
                
    
    for i in range(len(gb)):
        a, b = gb[i]
        union(a, b)
        
    for i in range(1, len(rep)):
        find(i)
        
    print(rep)
    d = Counter(rep[1:])
    ans = [float('inf'), float('-inf')]
    for i in d:
        if d[i] >= 2:
            ans[0] = min(ans[0], d[i])
            ans[1] = max(ans[1], d[i])
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
