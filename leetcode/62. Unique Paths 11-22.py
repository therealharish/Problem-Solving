# Simple recursion without DP - Gives TLE 
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        def recur(r, c):
            if(r>m or c>n):
                return 0
            if(r==m-1 and c==n-1):
                return 1
            else:
                return recur(r+1, c)+recur(r, c+1)
        
        ans = recur(0,0)
        return ans

# recursion with memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def recur(r, c):
            if(r>m or c>n):
                dp[(r,c)] = 0
                return 0
            if(r==m-1 and c==n-1):
                dp[(r,c)] = 1
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            dp[(r,c)] = recur(r+1, c)+recur(r, c+1)
            return dp[(r,c)]
        
        ans = recur(0,0)
        return ans