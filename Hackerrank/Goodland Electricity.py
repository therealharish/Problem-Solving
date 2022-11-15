#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons1(k, arr):
    i=0;
    count=0;
    while i<len(arr):
      flag=1;
      for j in range(i+k-1, i-k+2, -1):
        if(j<len(arr) and arr[j]==1):
          i=j+k
          count+=1;
          flag=0;
          break;
      if(flag):
        return -1
    return count

def pylons(k, arr):
    i = 0
    j = k-1
    count  = 0 
    poss=0
    while(poss<len(arr)-1):
        if(j>=len(arr)):
            j = len(arr)-1
        while(arr[j]!=1 and j>i):
            j-=1
        if(arr[j]==1):
            count+=1
            poss=k+j-1
            i = j + 1
            j = j + 2*k -1
        else:
            return -1
        
        # print(i, j, poss)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    
