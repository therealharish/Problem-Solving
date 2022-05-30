#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
  l=[]
  for i in range(1,len(a)):
    if(i==0):
      if(abs(a[i]-a[i+1])<=1):
        l.append(a[i])
    if(abs(a[i]-a[i-1])<=1):
      l.append(a[i])    
  print(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
