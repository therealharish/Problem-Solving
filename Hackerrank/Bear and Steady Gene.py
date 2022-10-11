# in notes 1 pg 32

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter 

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def valid(n, s):
  for x,y in s.items():
    if(y>n):
      return False
  return True
  

def steadyGene(gene):
  d = Counter(gene)
  n = len(gene)//4
  left = 0
  right = 0
  minString = len(gene)
  while(right < len(gene)):
    while(right < len(gene) and not valid(n, d)):
      char = gene[right]
      d[char]-=1
      right+=1
    while(left < len(gene) and valid(n, d)):
      char = gene[left]
      d[char]+=1
      left+=1
    minString = min(right - left + 1, minString)
  if(minString == len(gene)):
    return 0
  return minString
      
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
