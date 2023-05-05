#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    l = len(s)
    sqr = math.sqrt(l)
    m = math.floor(sqr)
    n = math.ceil(sqr)
    if(m*n<l):
      m+=1
    mat = [["" for j in range(n)] for i in range(m)]
    # print(mat)
    c = 0
    for i in range(m):
      for j in range(n):
        if(c < len(s)):
          mat[i][j] = s[c]
          c+=1
    # print(mat)
    newS = ""
    for i in range(n):
      for j in range(m):
        newS+=mat[j][i]
      newS+=" "

    return newS
  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
