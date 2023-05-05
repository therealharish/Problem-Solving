class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def recur(i, j):
            if(i+1==j):
                return 0
            ans = float('inf')
            if (i, j) in dp:
                return dp[(i, j)]
            else:    
                for k in range(i+1, j):
                    a = values[i]*values[j]*values[k] + recur(i, k) + recur(k, j)
                    ans = min(ans, a)
                dp[(i, j)] = ans
                return dp[(i, j)]
        dp = {}
        ans = recur(0, len(values)-1)
        return ans
        