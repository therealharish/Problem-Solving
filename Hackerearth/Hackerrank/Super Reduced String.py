#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
  l=[]
  i=0;
  while(i<len(s)):
    if(len(l)==0 or l[-1]!=s[i]):
      l.append(s[i])
    else:
      l.pop(-1)
    i+=1;
  if(len(l)==0):
    return "Empty String"
  else:
    return "".join(l)
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
