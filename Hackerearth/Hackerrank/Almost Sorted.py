#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def rev(ar, x, y):
  l = ar[x: y+1]
  l.reverse()
  n = ar[0:x]
  n.append(l)
  n.append(ar[y+1:])
  return n

def almostSorted(arr):
  cop = arr.copy()
  cop.sort()
  if(arr == sorted(arr)):
    print("yes")
    return
  x=0
  y=len(arr)-1
  while(x < len(arr) - 1 and arr[x] < arr[x+1]):
    x+=1
  while(y > 0 and arr[y-1] < arr[y]):
    y-=1
  arr[x], arr[y]=arr[y], arr[x]
  if(arr == sorted(arr)):
    print("yes")
    print("swap", x+1, y+1)
    return
  k = x+1
  l = y-1
  temp=arr.copy()
  while (k < l):
    temp[k], temp[l]= temp[l], temp[k]
    k+=1
    l-=1
  if(temp==sorted(temp)):
    print("yes")
    print("reverse", x+1, y+1)
    return
  print('no')
    
    
      
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
