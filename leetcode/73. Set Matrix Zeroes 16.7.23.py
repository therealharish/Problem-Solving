class Solutions1:
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
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = False
        for i in range(len(matrix)):
          if(matrix[i][0] == 0):
            col = True
          for j in range(1, len(matrix[0])):
              if(matrix[i][j]==0):
                matrix[0][j] = 0
                matrix[i][0] = 0
              

        for i in range(len(matrix)-1, -1, -1):
          for j in range(len(matrix[0])-1, 0, -1):
            if(matrix[0][j] == 0 or matrix[i][0] == 0):
                matrix[i][j] = 0
            
          if(col == True):
            matrix[i][0] = 0            
            

class Solution3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        setX = set()
        setY = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    setX.add(i)
                    setY.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i in setX or j in setY:
                    matrix[i][j] = 0
                    
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # col = matrix[0][]
        # row = matrix[][0]
        row = len(matrix)
        col = len(matrix[0])
        col0 = 1
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    
                    matrix[i][0] = 0
                    
                    if j!=0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
       
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] != 0:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j]=0
        
        if matrix[0][0] == 0:
            for j in range(col):
                matrix[0][j] = 0    
                
        if col0 == 0:
            for i in range(row):
                matrix[i][0] = 0
                
        
    
                    
        