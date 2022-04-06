#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def isTriangle(sides):
  a=sides[1]
  b=sides[2]
  c=sides[3]
  if (a + b < c) or (a + c < b) or (b + c < a):
        return False
  else:
        return True       
 
  

def maximumPerimeterTriangle(sticks):
  A = sticks.copy()
  A.sort()
  i=len(sticks)-3
  while i >= 0 and (A[i] + A[i+1] <= A[i+2]):
    i -= 1

  if i >= 0 :
      return([A[i],A[i+1],A[i+2]])
  else :
      return([-1])
    
  
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
