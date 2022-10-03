class Solutions:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indexes = ([], [])
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if(matrix[i][j]==0):
              indexes[0].append(i)
              indexes[1].append(j)
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if(i in indexes[0] or j in indexes[1]):
              matrix[i][j] = 0

# constant space solution optimized
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = False
        for i in range(len(matrix)-1, -1, -1):
          for j in range(len(matrix[0])-1, -1, -1):
            if(matrix[i][j]==0):
              if(matrix[i][0] = 0):
                col=True
              else:
                matrix[0][j] = 0
                matrix[i][0] = 0
              

        for i in range(len(matrix)-1, -1, -1):
          for j in range(len(matrix[0])-1, -1, -1):
            if(matrix[i][0] == 0 or matrix[0][j]==0):
              matrix[i][j]=0
            if(col == True):
              matrix[i][0] 0
            