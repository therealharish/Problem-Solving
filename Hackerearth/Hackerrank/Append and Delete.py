#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    x,y=len(s),len(t)
    p=0
    q=max(x,y)
    for i in range(q):
        if i<x and i<y and s[i]==t[i]:
            p+=1
        else:
            break
    if x+y<=k:
        return 'Yes'
    if k-(x+y-2*p)>=0:
        if (k-(x+y-2*p))%2==0:
            return 'Yes'
        else:
            return 'No'
    return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
#!/bin/python3
