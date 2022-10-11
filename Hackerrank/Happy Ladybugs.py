#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
  b=b+'_'
  d = Counter(b)
  if(d['_']==1):
    for i in range(1, len(b)-1):
      if b[i-1]!=b[i] and b[i+1]!=b[i]:
        return "NO"
        
  for x,y in d.items():
    if y==1 and x!='_':
      return "NO"
  
  return "YES"
    

  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
