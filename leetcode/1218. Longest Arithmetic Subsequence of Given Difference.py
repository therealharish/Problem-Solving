sys.setrecursionlimit(10**6)

# memoization
class Solution1:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        next = [-1 for _ in range(len(arr))]
        d = {}
        d[arr[0]] = 0
        next[0] = -1
        
        for i in range(1, len(arr)):
            print(d, next)
            if (arr[i] - difference) in d:
                next[i] = d[arr[i] - difference]
            d[arr[i]] = i
        print(d, next)
        @cache
        def f1(i):

            if i == 0:
                return 0
            return max(1 + f2(next[i-1]), f1(i-1))

        @cache
        def f2(i):

            if i == -1:
                return 0
            # print(i, next[i])
            return 1 + f2(next[i])

        return f1(len(arr))
    
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        next = [-1 for _ in range(len(arr))]
        d = {}
        d[arr[0]] = 0
        next[0] = -1
        
        for i in range(1, len(arr)):
            print(d, next)
            if (arr[i] - difference) in d:
                next[i] = d[arr[i] - difference]
            d[arr[i]] = i
        print(d, next)
        
        f1 = [0] * (len(arr)+1)
        f2 = [0] * (len(arr)+1)
        for i in range(len(arr)-1, -1, -1):
            f1[i] = max(f1[i+1], f2[next[i]] + 1)
            f2[i] = 1 + f2[next[i]]
        return f1[0]
            
        
            