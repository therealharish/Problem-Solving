class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      pointer
      for i in range(len(matrix)):
        if target < matrix[i][-1]:
          pointer = i
      l = 0
      r = len(matrix[pointer])-1
      while(l<=r):
        mid = (l+r)//2
        if(matrix[pointer][mid] == target):
          return True
        elif(matrix[pointer][mid] > target):
          r = mid - 1
        else:
          l = mid + 1
      return False