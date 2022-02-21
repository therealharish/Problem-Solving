#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
  if(len(arr)%2==0):
    return 0
  else:
    for i in range

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
