#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
  mi = min(x)
  ma = max(x)
  s = set(x)
  low = mi
  mid = mi+k
  count = 0
  while(low<=ma):
    if(mid in s):
      count+=1
      low = mid + k +1
      while(low not in s and low<=ma):
        print(low)
        low+=1
      mid = low+k
    else:
      mid-=1
  return count
    
      
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
