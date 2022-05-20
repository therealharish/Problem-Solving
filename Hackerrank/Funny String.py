#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
  check = s
  l=[]
  for i in range(len(s)-1):
    j=i+1
    l.append(abs(ord(s[i])-ord(s[j])))
             
  check = s[::-1]
  for i in range(len(check)-1):
    j=i+1
    l.append(abs(ord(s[i])-ord(s[j])))
  if(l==l[::-1]):
    return "Funny"
  else:
    return "Not Funny"    

             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
