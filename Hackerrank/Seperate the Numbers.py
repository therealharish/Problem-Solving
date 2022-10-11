#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
  
  for i in range(1, len(s)//2+1):
    x=s[0:i]
    news=x
    num = int(x)
    while(len(news)<len(s)):
      num+=1;
      news+=str(num)
    if(news==s):
      print("YES", s[0:i]);
      return
  print("NO")
  
    
  

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
