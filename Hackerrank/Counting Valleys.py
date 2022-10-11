#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
  sea = 0
  i=0;
  count=0
  while(i<len(path)):
    if(path[i]=="U"):
      sea+=1;
    else:
      sea-=1
    if(sea==0 and i!=0 and path[i]!="D"):
      count+=1
    i+=1
  return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
