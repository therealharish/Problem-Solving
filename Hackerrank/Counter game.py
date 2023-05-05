#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
def isPowerOfTwo(x):
    return x&(x-1)==0

def counterGame(n):
  move = 1
  newN = n
  while(newN):
    if(not isPowerOfTwo(newN)):
      b = bin(newN)[2:]
      newN = newN - 2**(len(b)-1)
    else:
      newN = newN//2
    move+=1
  if(not move&1):
    return "Richard"
  else:
    return "Louise"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()



# 5
# 1560834904
# 1768820483
# 1533726144
# 1620434450
# 1463674015
# Expected Output

# Download
# Richard
# Richard
# Louise
# Richard
# Louise