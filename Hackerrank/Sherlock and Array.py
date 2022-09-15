#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
  l = 0
  r = len(arr)-1
  sl = 0
  sr = 0
  while(l<=r):
    if(sr==sl):
      if(l==r):
        return "YES"
      else:
        if(arr[r]==0):
          r-=1
        elif(arr[l]==0):
          l+=1
        else:
          sr+=arr[r]
          sl+=arr[l]
          l+=1
          r-=1
    elif(sl>sr):
      sr+=arr[r]
      r-=1
    else:
      sl+=arr[l]
      l+=1
  return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
