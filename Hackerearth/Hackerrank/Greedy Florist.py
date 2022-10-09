#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
  ans = 0
  rev = sorted(c, reverse = True)
  i = 0
  count = 1
  kcopy = k
  while(i<len(c)):
    ans+=(count*rev.pop(0))
    k-=1
    i+=1
    if(k==0):
      count+=1
      k = kcopy
    
  return ans
    
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
