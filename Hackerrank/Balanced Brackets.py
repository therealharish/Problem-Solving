#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    open = ['(', '[', '{']
    closed = {
        ')':'(',
        ']':'[',
        '}':'{'
      }
    if(s[0] in closed):
      return "NO"
    
    st = []  
    for i in s:
      # print(st)
      if i in open:
        st.append(i)
      else:
        if(st and st[-1]==closed[i]):
          st.pop()
        else:
          return "NO"
    if(not st):
      return "YES"
    else:
      return "NO"
        
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

# 6
# }][}}(}][))]
# [](){()}
# ()
# ({}([][]))[]()
# {)[](}]}]}))}(())(
# ([[)
# Expected Output

# Download
# NO
# YES
# YES
# YES
# NO
# NO