#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def finddiff(a,b):
  count=0
  for i in range(len(a)):
    if(a[i]!=b[i]):
      count+=1
  return count

def highestValuePalindrome(s, n, k):
  l = list(s)
  
  s1 = l[:n//2]
  s2 = l[n//2:]
  i=0
  if(len(s)%2!=0):
    leverage = [s2.pop(0)]
  else:
    leverage = []
    
  s2.reverse()
  diff = finddiff(s1, s2)
  
  if(diff>k):
    return "-1"
    
  while(k and diff<=k):
    
    if(k>1):
      if(k>diff):
        if(s1[i]!='9' and s2[i]!='9'):
          if(s1[i]==s2[i]):
            diff+=1
          s1[i]='9'
          s2[i]='9'
          k-=2
          diff-=1
        elif(s1[i]=='9' and s2[i]!='9'):
          s1[i]='9'
          k-=1
          diff-=1
        elif(s2[i]=='9' and s1[i]!='9'):
          s2[i]='9'
          k-=1
          diff-=1
          
      elif(k==diff):
        if(s1[i]<s2[i]):
          s1[i] = s2[i]
          k-=1
          diff-=1
        elif(s1[i]>s2[i]):
          s2[i] = s1[i]
          k-=1
          diff-=1
          
    elif(k==1):
      if(n%2!=0):
        leverage = ['9']
        k-=1
        
      else:
        if(s1[i]<s2[i]):
          s1[i] = s2[i]
          k-=1
          diff-=1
        elif(s1[i]>s2[i]):
          s2[i] = s1[i]
          k-=1
          diff-=1
    
        
    i+=1

  s=''.join(s1+leverage+s2[::-1])
  if(s!=s[::-1]):
    return "-1"
  else:
    return s
      
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
