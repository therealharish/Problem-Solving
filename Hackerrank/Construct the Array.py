#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
  if(x!=1):
    A = [0]*n
    B = [1]*n
  if(x==1):
    A=[1]*n
    B=[0]*n
  mod = 10**9 + 7
  for i in range(1, n):
    A[i] = B[i-1]%mod
    B[i] = ((A[i-1]+B[i-1])*(k-1) - A[i])%mod
  return A[-1]%mod
    
    
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
