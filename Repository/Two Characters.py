#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
  stringSet = set()
  for i in s:
    stringSet.add(i)
  l = list(stringSet)

  def validString(li):
    lastChar = '0'
    count = 0
    for i in s:
      if i in li:
        if i == lastChar:
          return 0
        count+=1
        lastChar = i
    return count
        
        
  m = 0

  for i in range(len(l)-1):
    for j in range(i+1, len(l)):
      m = max(m, validString([s[i], s[j]]))
  return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
