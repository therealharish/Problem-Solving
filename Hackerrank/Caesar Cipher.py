#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
  newstr = ""
  for i in s:
    if i.isalpha():
      c=ord(i)
      c=c+k%26
      if i.islower() and c>122:
        c=c-26
      elif i.isupper() and c>90:
        c=c-26
      c=chr(c)
      newstr+=c
    else:
      newstr+=i
  return newstr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
