#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
def listDivisors(n) :
    i = 1
    l=[]
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) :
                l.append(i)
            else :
                l.append(i)
                l.append(n//i)
        i = i + 1
    return l

def solve(a):
  d={}
  d[a[0]]=0
  maxele = max(a)
  for i in range(len(a)):
    if i == 0:
      continue
    else:
      a[i]=a[i-1]+a[i]
    d[a[i]]=0

  su = a[-1]

  l = listDivisors(su)
  newl=[]
  for i in l:
    if i >= maxele:
      copy=i
      flag=0
      while(copy<su):
        if(copy not in d):
          flag=1
          break
        else:
          copy+=i
      if not flag:
        newl.append(i)
  return sorted(newl)
      
    
  
      
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
