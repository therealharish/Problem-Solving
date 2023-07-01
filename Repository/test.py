from typing import *


def binaryQueries(n: int, a: List[int], q: int, queries: List[List[int]]) -> List[int]:
    result = []
    
    


    for query in queries:
        left = query[0]
        right = query[1]
        x = query[2]

        for i in range(left, right+1):
            a[i] ^= x

        orResult = a[left]
        for i in range(left + 1, right+1):
            orResult |= a[i]

        result.append(orResult)

    return result


    