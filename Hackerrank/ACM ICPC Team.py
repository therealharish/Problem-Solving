#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def countsub(s1, s2):
    newstr=""
    b = int(s1,2)|int(s2,2)
    newstr = bin(b)
    count = newstr.count("1")
    return count;
        
        

def acmTeam(topic):
    teams=0;
    count=0;
    m=0; #stores max value
    maxl=[];
    for i in combinations(topic, 2):
            count = countsub(i[0], i[1])
            maxl.append(count);
            if(m <= count):
                m = count;
    teams = maxl.count(m)
    l=[m, teams]
    return l
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
