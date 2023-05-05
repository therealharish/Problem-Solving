#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
  ma, mi = scores[0], scores[0]
  macount = 0
  micount = 0
  for i in range(len(scores)):
    if(scores[i]<mi):
      mi = scores[i]
      micount+=1
    if(scores[i]>ma):
      ma = scores[i]
      macount+=1
  return [macount, micount]
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
