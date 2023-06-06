#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    freq = {}
    notice = 0

    def find(k):
        for i in range(201):
            if i in freq:
                k-=freq[i]
            if k < 0:
                return i

    for i in range(len(expenditure)-1):
        if expenditure[i] in freq:
            freq[expenditure[i]] += 1
        else:
            freq[expenditure[i]] = 1
            
        if i+1 >= d:
            
            if d%2==0:
                median = (find((d//2) - 1) + find(d//2))/2
            else:
                median = find(d//2) 
                
            print(median)
                
            if expenditure[i+1] >= 2*median:
                notice += 1
            
            freq[expenditure[i-d+1]] -= 1
                
    return notice
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()