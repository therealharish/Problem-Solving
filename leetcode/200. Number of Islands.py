class Solution:
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