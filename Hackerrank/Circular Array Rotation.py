#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def reverseArray(arr, l, h):
  while(l<=h):
    arr[l], arr[h]=arr[h], arr[l];
    l+=1;
    h-=1;
  return arr


def circularArrayRotation(a, k, queries):
  # a = reverseArray(a,0,len(a)-1)
  # a = reverseArray(a, 0, k-1)
  # a = reverseArray(a, k, len(a)-1)
  b=[];
  for i in a:
    b.append(i)
  for i in range(len(a)):
    b[(i+k)%(len(a))] = a[i]
  l=[];
  for i in queries:
    l.append(b[i])
  return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
