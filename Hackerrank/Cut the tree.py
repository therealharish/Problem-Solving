#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    adj = {i:[] for i in range(1, len(data)+1)}
    for src, dst in edges:
        adj[src].append(dst)
        
    for i in range(1, len(data)+1):
        print(i, adj[i])

    s = []
    
    def solve(i):
        if not i:
            return 0
        return data[i-1] + sum(solve(j) for j in adj[i])
    
    for i in range(1, len(data)+1):
        print(i, solve(i))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
