#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        count = 0
        m -= 1
        while(True):
            if count < k:
                count += n
                n-=1
            if count < k:
                count += m
                m-=1
            if count >= k:
                break
        print(count)