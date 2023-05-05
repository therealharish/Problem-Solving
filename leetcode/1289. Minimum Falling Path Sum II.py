class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        def solve(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return float('inf')
            if i == row-1:
                return grid[i][j]
            res = float('inf')
            for k in range(col):
                if k == j:
                    continue
                else:
                    res = min(res, solve(i+1, k))
            return grid[i][j] + res

        ans = float('inf')                
        for i in range(col):
            ans = min(ans, solve(0, i))
        return ans
