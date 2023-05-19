class Solution1:
    def numIslands(self, matrix: List[List[str]]) -> int:
      def dfs(i,j):
        if(i<0 or i>len(matrix)-1 or j<0 or j>len(matrix[0])-1 ):
          return
        if(matrix[i][j]=="0"):
          return
        if(matrix[i][j]=="1"):
          matrix[i][j]="2"
          dfs(i-1, j)
          dfs(i+1, j)
          dfs(i, j-1)
          dfs(i, j+1)



          
      count = 0
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          if (matrix[i][j]=="1"):
            count+=1
            dfs(i,j)
      return count
    
    
class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
      row = len(matrix)
      col = len(matrix[0])
      visited = [0 for j in range(col) for i in range(row)]
      directions = [[0,1],[0,-1],[1,0],[-1,0]]
      
      def dfs(i, j, count):
        if i >= row or j >= col or i < 0 or j < 0 or visited[i][j] != 0 or matrix[i][j] == '0':
          return
        visited[i][j] = count
        for r, c in directions:
          dfs(i+r, j+c, count)
      
      count = 0
      for i in range(row):
        for j in range(col):
          if visited[i][j] == 0:
            dfs(i, j, count+1)
            
      return count
          
      
        
        
      