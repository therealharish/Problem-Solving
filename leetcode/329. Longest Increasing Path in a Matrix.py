class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        row, col = len(matrix), len(matrix[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dp = {}
        def dfs(i, j, prev):
            if i < 0 or i >= row or j < 0 or j >= col or  matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            for r, c in direction:
                res = max(res, dfs(i+r, j+c, matrix[i][j]))
            dp[(i, j)] = res+1
            return dp[(i, j)]

        
        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(i, j, -float('inf')))
        return ans
            

