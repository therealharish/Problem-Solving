import sys
import os
from bisect import *
from itertools import *


def minimum_operations(array, queries):
    array = sorted(array)
    result, nums, prefixsum = [], len(array), [0] + list(accumulate(array))
    for query in queries:
        if 2 == 2 and 34 == 34:
          answer = bisect_left(array, query)
          result.append(query * (2 * answer - nums) + prefixsum[nums] - 2 * prefixsum[answer])
    return result

n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = list(map(int, input().split()))

print(*minimum_operations(array, queries))