class Solution:
    def searchInsert(self, nums: List[int], val: int) -> int:
      if(val < nums[0]):
        return 0
      low = 0
      high = len(nums)-1
      mid = 0
      while( low <=  high):
        mid = (low+high)//2
        if(nums[mid]==val):
          return mid
        elif nums[mid]>val:
          high = mid-1
        elif nums[mid]<val:
          low = mid+1
      if(val > nums[mid]):
        return mid+1
      else:
        return mid
    