#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
  # count=0;
  # # //check right
  # i = r_q;
  # j= c_q+1;
  # for x in range(j, n+1):
  #   if([i,x] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  # # //check left
  # i = r_q
  # j=c_q-1
  # for x in range (j, 0, -1):
  #   if([i,x] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  # #check above
  # i=r_q-1;
  # j=c_q;
  # for x in range(i, 0, -1):
  #   if([x,j] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  # #check below
  # i=r_q+1
  # j=c_q
  # for x in range(i, n+1):
  #   if([x,j] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  # #check north west
  # i=r_q-1
  # j=c_q-1;
  # while(i>=1 and j>=1):
  #   if([i,j]  in obstacles):
  #     break;
  #   else:
  #     count+=1;
  #   i-=1;
  #   j-=1;
  # #check north east
  # i=r_q-1
  # j=c_q+1;
  # while(i>=1 and j<n+1):
  #   if([i,j] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  #   i-=1;
  #   j+=1;
  # #check south west
  # i=r_q+1
  # j=c_q-1;
  # while(i<n+1 and j>=1):
  #   if([i,j] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  #   i+=1;
  #   j-=1;
  # #check south east
  # i=r_q+1
  # j=c_q+1;
  # while(i<n+1 and j<n+1):
  #   if([i,j] in obstacles):
  #     break;
  #   else:
  #     count+=1;
  #   i+=1;
  #   j+=1;
  # return count


  count = 0;
  r= n-c_q;
  l= c_q-1;
  u= n-r_q;
  d= r_q-1;
  dlu= min(u,l)
  dru = min(u, r)
  dld = min(l, d)
  drd = min(r, d)
  
  

  
    
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
