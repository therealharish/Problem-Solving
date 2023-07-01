from typing import *


def contributions(n: int, arr: List[int]) -> int:
    m1, m2, m3 = [], [], []
    
    def findSum(arr, n):
        total_sum = 0
        for i in range(32):
            zc, oc, idsum = 0, 0, 0
            for j in range(n):
                if arr[j] % 2 == 0:
                    zc += 1
                else:
                    oc += 1
                arr[j] //= 2
            idsum = oc * zc * (1 << i)
            total_sum += idsum
        return total_sum
    
    for i in range(n):
        if arr[i]%3==0:
            m1.append(arr[i])
        elif arr[i]%3==1:
            m2.append(arr[i])
        else:
            m3.append(arr[i])
            
    totalSum = 0
    totalSum += findSum(m1, len(m1))
    totalSum += findSum(m2, len(m2))
    totalSum += findSum(m3, len(m3))
    
    
    return totalSum
    