#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
  rev=sorted(arr, reverse=True)
  i=0;
  pos = 0
  d = {}
  for j in range(len(arr)):
    d[arr[j]]=j
  while(i<len(arr) and k):
    x=rev[pos]
    index = d[x]
    if(arr[i]<x):
      d[arr[index]], d[arr[i]] = d[arr[i]], d[arr[index]]
      arr[index], arr[i]=arr[i], arr[index]
      k-=1;
    i+=1
    pos+=1
      
  return arr
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
