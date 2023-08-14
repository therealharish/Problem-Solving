# old 
class Solution1:
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

# 29, 03, 2023
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            if word1[m-1] == word2[n-1]:
                return solve(m-1, n-1)
            else:
                return 1 + min(solve(m-1, n-1), solve(m-1, n), solve(m, n-1))
        return solve(len(word1), len(word2))
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(i, j):
            if i == 0:
                return j
            if j == 0:
                return i
            print(i, j)
            if word1[i-1] == word2[j-1]:
                return solve(i-1, j-1)
            return min(solve(i-1, j-1), solve(i-1, j), solve(i, j-1)) + 1
        
        return solve(len(word1), len(word2))