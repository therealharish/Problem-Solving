class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def solve(m, n):
            if(m == 0):
                return n
            if(n==0):
                return m
            if((m,n) in dp):
                return dp[(m,n)]
            if(word1[m-1]==word2[n-1]):
                dp[(m, n)] = solve(m-1, n-1)
                return dp[(m, n)]
            else:
                dp[(m, n)] = 1 + min(solve(m-1, n), solve(m-1,n-1), solve(m, n-1)) 
            return dp[(m, n)]
        
        return solve(len(word1), len(word2))