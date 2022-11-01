class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

      def dfs(r, c):

        if(r==len(grid)-1):
          return c
        elif(c==len(grid[0])-1 and grid[r][c] == 1):
          return -1
        elif(c==0 and grid[r][c] == -1):
          return -1
        elif(grid[r][c]!=grid[r][c+1]):
          return -1
          
        elif(r>len(grid) or c>len(grid[0]) or r<0 or c<1):
          return -1
        else:
          if(grid[r][c]==1):
            return dfs(r+1, c+1)
          else:
            return dfs(r-1. c-1)

      ans = []
      for c in range(len(grid[0])):
        ans.append(dfs(0, c))
      return ans
      