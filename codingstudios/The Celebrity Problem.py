Almost Sorted
from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):
    st = []
    for i in range(n):
        st.append(i)

    while(len(st)>1):
        first = st.pop()
        second = st.pop()
        if(knows(first, second)):
            st.append(second)
        else:
            st.append(first)

    possible = st.pop()
    for i in range(n):
        if(i!=possible and knows(possible, i)):
            return -1
        if(i!=possible and not knows(i, possible)):
            return -1
    return possible
