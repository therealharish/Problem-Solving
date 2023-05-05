#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    count = 0
    if(m==1 and w==1):
      count+=(p-1)
      m=2
    while(m*w<n):
      count+=1
      product = m*w
      p1= product//p
      p2 = (product-p1)//2
      if(p1>p2):
        p1,p2=p2,p1
        
      if(m<=w):
        m+=p2
        w+=p1
      else:
        m+=p1
        w+=p
    return count+1
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
