#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
  s = 0
  for i in range(len(q)-1, -1, -1):
    if(q[i] - i - 1 > 2):
      print("Too chaotic")
      return
    for j in range(max(0, q[i]-2), i): 
      # because the element could have only moved two positions ahead of itself, we check if any element is two position ahead of the current element, because the element after it could only go to one position ahead of the current element's initial position. Hence q[i]-1 is the boundary to check
      if(q[j]>q[i]):
        s+=1
  
  print(s)
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
