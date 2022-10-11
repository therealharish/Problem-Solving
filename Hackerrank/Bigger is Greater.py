#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def biggerIsGreater(w):
    st = [w[-1]]
    p = len(w) - 2
    print(len(w), p)
    newStr = ""
    l = []
    while (p >= 0):
        print(w[p], st)
        if (ord(st[-1]) > ord(w[p])):
            while (st and ord(st[-1]) > ord(w[p])):
                l.append(st[-1])
                st.pop()
            st.append(w[p])
            if (st):
                newStr = st[-1]
                st.pop()
            print(newStr, w[p])
            newStr += "".join(st)
            print(newStr)

            newStr += "".join(l)
            print(newStr)

            newStr = w[:p] + newStr
            return newStr

        st.append(w[p])
        p -= 1
    return "false"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
