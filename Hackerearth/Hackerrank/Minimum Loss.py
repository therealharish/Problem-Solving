#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
  d={}
  for i in range(len(price)):
    d[price[i]]=i
  price.sort()
  mi=10**16;
  for i in range(1, len(price)):
    if(price[i]-price[i-1]<mi and d[price[i]]
<d[price[i-1]]):
      mi=price[i]-price[i-1]
  return mi
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
