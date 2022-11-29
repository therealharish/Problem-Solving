#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#

def findMask(num):
    mask = 0
    for j in num:
        mask = mask | (1 << (ord(j) - ord('0')))
    return mask
    
def winningLotteryTicket(tickets):
    mask = [0]*1024
    for i in tickets:
        m = findMask(i)
        mask[m]+=1
    
    ans = 0
    for i in range(len(mask)):
        for j in range(i+1, len(mask)):
            if(i|j == 1023):
                ans+=mask[i]*mask[j]
    if(mask[1023]):
        ans+=math.comb(mask[1023], 2)
    return ans
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
