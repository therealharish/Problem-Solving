class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      row = len(heights)
      col = len(heights[0])
      pac = set()
      atl = set()
      res = []

      def dfs(r, c, visited, prevHeight):
        if(r<0 or c<0 or r>row-1 or c>col-1):
          return
        if(heights[r][c] < prevHeight):
          return
        if((r,c) in visited):
            return
        visited.add((r,c))
        print(visited)
        dfs(r-1, c, visited, heights[r][c])
        dfs(r+1, c, visited, heights[r][c])
        dfs(r, c-1, visited, heights[r][c])
        dfs(r, c+1, visited, heights[r][c])

      
      for c in range(col):
        dfs(0, c, pac, heights[0][c])
        dfs(row-1, c, atl, heights[row-1][c])

      for r in range(row):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, col-1, atl, heights[r][col-1])

      for i in range(row):
        for j in range(col):
          if((i,j) in pac and (i,j) in atl):
            res.append([i,j])
      return res
            
            
    