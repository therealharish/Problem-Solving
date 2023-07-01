#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def printIt(x):
    for i in x:
        print(i, x[i])

def reverseShuffleMerge(s):
    avail = {}
    req = {}
    used = {}
    
    d = Counter(s)
    for i in d:
        avail[i] = d[i]
        req[i] = d[i]//2
        used[i] = 0
        
    print("Avail")
    printIt(avail)
    print("Req")
    printIt(req)
    print("Used")
    printIt(used)
    
    st = []
    for i in range(len(s)-1, -1, -1):
        curr = s[i]
        while (st and (used[curr] < req[curr]) and (ord(curr) < ord(st[-1])) and (avail[st[-1]] > req[st[-1]] - used[st[-1]])):
            # print(st[-1], used[st[-1]], avail[st[-1]], req[st[-1]]) 
            used[st[-1]] -= 1
            st.pop()
        if used[curr] < req[curr]:
            st.append(curr)
            used[curr] += 1
        avail[curr] -= 1
    return ''.join(st)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

