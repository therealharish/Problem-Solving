#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
  d={}
  ans=[]
  count=1
  for i in range(len(orders)):
    serve = orders[i][0] + orders[i][1]
    if(serve in d):
      d[serve].append(count)
      count+=1
    else:
      d[serve]=[count]
      count+=1

  dict = OrderedDict(sorted(d.items()))
  for x,y in dict.items():
    if(len(y)==1):
      ans.append(y[0])
    else:
      for i in y:
        ans.append(i)
  return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
