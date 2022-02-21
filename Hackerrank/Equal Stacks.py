#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
  h1.reverse()
  h2.reverse()
  h3.reverse()
  for i in range(1,len(h1)):
    h1[i]=h1[i-1]+h1[i]
  for i in range(1,len(h2)):
    h2[i]=h2[i-1]+h2[i]
  for i in range(1,len(h2)):
    h2[i]=h2[i-1]+h2[i]
  h1.reverse()
  h2.reverse()
  h3.reverse()
  mi=min(len(h1), len(h2), len(h3))
  for _ in range(mi)
   if(h1[_] in h2 and h1[_] in h3):
    return h1[_]
    break;
  return 0
      
    
    
      

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print(result)
