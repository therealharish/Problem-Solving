#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
  d = collections.Counter(arr)
  m = max(list(d.values()))
  l=[]
  for x,y in d.items():
    if(y==m):
      l.append(x)
  return min(l)
  
    
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
