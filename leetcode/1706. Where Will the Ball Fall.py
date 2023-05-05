class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

      def dfs(r, c):

        if(r >= len(grid)):
          return c
        if(c<len(grid)-1 and grid[r][c]==1 and grid[r][c+1]==1):
          return dfs(r+1, c+1)
        if(c>0 and grid[r][c]==-1 and grid[r][c-1]==-1):
          return dfs(r+1, c-1)
        if(c>=len(grid[0])-1 and grid[r][c] == 1):
          return -1
        else:
          return -1

      ans = []
      for c in range(len(grid[0])):
        ans.append(dfs(0, c))
      return ans
      