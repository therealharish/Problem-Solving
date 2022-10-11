#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countmin(arr, temp, h):
  ans=0;
  for i in range(n):
      if (arr[i] != temp[i]):
          ans += 1
          init = arr[i]
          # If not, swap this element
            # with the index of the
            # element which should come here
          arr[i], arr[h[temp[i]]] = arr[h[temp[i]]], arr[i]

          # Update the indexes in
            # the hashmap accordingly
          h[init] = h[temp[i]]
          h[temp[i]] = i 
  return ans

def lilysHomework(arr):
  ans = []
  temp = arr.copy()
  temp.sort()
  h = {}
  for i in range(n):
      h[arr[i]] = i
  ans.append(countmin(arr, temp, h))
  temp = arr.copy()
  temp.sort(reverse = True)
  for i in range(n):
      h[arr[i]] = i
  ans.append(countmin(arr, temp, h))
  return min(ans)
  
    
    
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
