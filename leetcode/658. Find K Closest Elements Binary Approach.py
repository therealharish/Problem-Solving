class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      low = 0
      high = len(arr)-k
      while(low<high):
        mid = (low+high)//2
        if(x-arr[mid]<=arr[mid+k]-x):
            
#             i put <= because if x-arr[mid]==x-arr[mid+k] then we can't just leave it or we'll end up losing that value if it goes into the low part
            high = mid
        else:
          low = mid+1
      return arr[low:low+k]
            
            