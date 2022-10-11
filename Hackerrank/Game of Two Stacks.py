#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
  def prefixSum(l):
    ps = [0]*(len(l)+1)
    for i in range(len(l)):
      ps[i+1]=l[i]+ps[i]
    return ps

  a = prefixSum(a)
  b = prefixSum(b)
  x = 0
  y = 0
  while(x<len(a) and a[x+1]<=maxSum):
    x+=1
  ans = x
  for i in range(x, -1, -1):
    while(y<len(b) and b[y+1]+a[i] <=maxSum):
      y+=1
    if(ans<i+y):
      ans = i+y
  return ans

# s = 0
  # ac=0
  # bc=0
  # for i in range(len(a)):
  #   s=s+a[i]
  #   ac+=1
  #   if(s>maxSum):
  #     break
  # res = ac
  # for i in range(len(b)):
  #   s = s+b[i]
  #   bc+=1
  #   while(s>maxSum and ac>0):
  #     s-=a[ac-1]
  #     ac-=1
  #   if(s<maxSum):
  #     res = max(res, ac+bc)
  # return res
      
      
    
    
      
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
