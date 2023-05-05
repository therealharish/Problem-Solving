class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if i == 0:
            if(i==0 and j==0):
              continue
            else:
              grid[i][j]+= grid[i][j-1]
          elif j==0:
            if i==0 and j==0:
              continue
            else:
              grid[i][j]+=grid[i-1][j]
          else:
            a = grid[i][j]
            grid[i][j] = min(grid[i-1][j]+a, grid[i][j-1]+a)

      return grid[-1][-1]
              