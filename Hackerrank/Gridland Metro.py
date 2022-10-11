#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
  spots = n*m;
  l=[]
  d=dict();
  for x, y, z in track:
    if(x not in d.keys()):
      d[x]=(y,z)
    else:
      if(d[x][0]>z or d[x][1]<y):
        l.append((y,z))
      else:
        d[x]=(min(y, d[x][0]), max(z, d[x][1]))
  for i,j in d.values():
    length = j-i + 1
    spots-=length
  for i,j in l:
    length = j-i + 1
    spots-=length
  return spots
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
