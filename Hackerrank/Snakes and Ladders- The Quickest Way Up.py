#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    
    d = {}
    for x, y in ladders:
        d[x] = y
    for x, y in snakes:
        d[x] = y

    visited = set()
    q = deque()
    q.append(1)
    visited.add(1)
    count = 0
    while(q):
        count += 1
        for i in range(len(q)):
            i = q.popleft()
            if i == 100:
                return count-1
            for j in range(1, 7):
                if i+j in d and i+j not in visited:
                    q.append(d[i+j])
                    visited.add(d[i+j])
                elif i+j <= 100 and i+j not in visited:
                    q.append(i+j)
                    visited.add(i+j)
    
    return -1            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
