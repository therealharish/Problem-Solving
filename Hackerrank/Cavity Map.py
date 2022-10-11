#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
  arr = [[0 for c in range(len(grid[0]))] for r in range(len(grid))]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if(i==0 or j==0 or i == len(grid)-1 or j==len(grid[0])-1):
        arr[i][j]=str(grid[i][j])
      else:
        u = grid[i-1][j]
        d = grid[i+1][j]
        l = grid[i][j-1]
        r = grid[i][j+1]
        x = grid[i][j]
        if(x>u and x>d and x>l and x>r):
          arr[i][j]='X'
        else:
          arr[i][j]=str(grid[i][j])
  ans = []
  for i in range(len(arr)):
    s=''
    for j in range(len(arr[0])):
      s+=arr[i][j]
    ans.append(s)
  return ans
  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
