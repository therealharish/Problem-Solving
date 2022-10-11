#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factors(n) :
     
    l=[n];
    i = 2
    while i <= math.sqrt(n):
        if (n % i == 0) : 
          if (n / i == i) :
              l.append(i)
          else:
              l.append(i)
              l.append(int(n/i))
        i = i + 1
    return l

def downToZero(n):
  count=0;
  while(n>0):
    m = min(factors(n))
    if(m==n):
      n=n-1;
    else:
      n=m
    count+=1
  return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
