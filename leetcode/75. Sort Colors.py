# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#       x = nums.count(0)
#       y = nums.count(1)
#       z = nums.count(2)
#       xx = [0]*x
#       yy = [1]*y
#       zz = [2]*z

#       xx.extend(yy)
#       xx.extend(zz)

#       nums[:] = xx


class Solution:
    def sortColors(self, nums: List[int]) -> None:
      low = 0
      high = len(nums) -1
      mid = 0
      while(mid<=high):
        if(mid == 0):
          nums[low], nums[mid] = nums[mid], nums[low]
          low+=1
          mid+=1
        elif(mid==1):
          mid+=1
        elif(mid==2):
          nums[mid], nums[high] = nums[high], nums[mid]
          high-=1
      
        