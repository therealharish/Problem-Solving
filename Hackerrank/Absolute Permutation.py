#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
  arr = [i+1 for i in range(n)]
  if(k==0):
    return arr
  if(n%(2*k)!=0):
    return [-1]
  else:
    i = 0
    j = 0
    while(i<n):
      for j in range(i, i+k):
        arr[i], arr[j+k] = arr[j+k], arr[i]
        i+=1
      i+=k
    return arr
      
      
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
