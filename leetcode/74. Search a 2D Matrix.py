class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      pointer = -1
      if target > matrix[-1][-1]:
          return False
      l = 0
      h = len(matrix)-1
      while(l<h):
          mid = (l+h)//2
          if(matrix[mid][-1]>=target):
              h = mid
          else:
              l = mid+1
      pointer = l
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


# in notes 1 last page
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n -1 
        while(low<=high):
            mid = (low+high)//2
            i = mid//n
            j = mid%n
            if(matrix[i][j] == target):
                return True
            if(matrix[i][j]>target):
                high = mid-1
            else:
                low = mid+1
        return False