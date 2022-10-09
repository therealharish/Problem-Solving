#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heapify, heappush, heappop

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
  # A.sort()
  # swaps=0;
  # while(A[0]<k):
  #   s=int(A[0]+(2*A[1]))
  #   A.pop(0)
  #   A.pop(0)
  #   A.append(s)
  #   A.sort()
  #   swaps+=1;
  # return swaps

  heapify(A)
  swaps=0;
  while(A[0]<k):
    if(len(A)<2):
      return -1;
    heappush(A, heappop(A)+2*heappop(A))
    swaps+=1
  return swaps
  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
