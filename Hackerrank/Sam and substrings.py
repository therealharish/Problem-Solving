#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
  dp = []
  mod = 10**9 + 7
  dp.append(int(n[0]))
  for i in range(1,len(n)):
    s = (10 * dp[i-1] + int(n[i])*(i+1))%mod
    dp.append(s)
  return sum(dp)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
