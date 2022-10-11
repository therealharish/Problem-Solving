#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    countfr = 0;
    for i in range(1,n+1):
      if(i%2==0):
        countfr+=1
      if(i==p):
        break
    countba = 0
    for i in range(n, 0, -1):
      if(i==p):
        break
      if(i%2==0):
        countba+=1
    if(countba<countfr):
      return countba
    else:
      return countfr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
