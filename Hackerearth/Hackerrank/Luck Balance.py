#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
  contests = sorted(contests, key = lambda x: x[0], reverse = True)
  print(contests)
  luck = 0
  for i in range(len(contests)):
    if(contests[i][1]==1 and k>0):
      luck+=contests[i][0]
      k-=1
    elif(contests[i][1]==1 and k==0):
      luck-=contests[i][0]
      continue
    else:
      luck+=contests[i][0]
  return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
