# in notes 1 pg 7
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      left = 0
      right = len(nums)-1
      i = len(nums)-1
      ans = [0]*len(nums)
      while(left<=right):
        lsquare = nums[left]**2
        rsquare = nums[right]**2
        if(lsquare>rsquare):
          ans[i] = lsquare
          left+=1
        elif(rsquare>lsquare):
          ans[i] = rsquare
          right-=1
        else:
          ans[i] = rsquare
          right-=1
        i-=1
      return ans
          
        
        