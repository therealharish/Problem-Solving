#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
  d = {}
  for i in astronaut:
    if(i[0] in d):
      d[i[0]].append(i[1])
    else:
      d[i[0]] = [i[1]]
    if(i[1] in d):
      d[i[1]].append(i[0])
    else:
      d[i[1]] = [i[0]]
  
  for i in range(n):
    if(i not in d):
      d[i] = []


  def dfs(l, source, visited):
    if source not in visited:
      l.append(source)
      visited.add(source)
      for vertex in d[source]:
        dfs(l, vertex, visited)

  count = 0 
  visited = set()
  ans = []
  for i in d:
    if(i not in visited):
      count+=1
      l = []
      dfs(l, i, visited)
      ans.append(l)

  s = 0
  result = 0
  for i in ans:
    result+= s*len(i)
    s+=len(i)
  return(result)

  
        
    
    
    
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
