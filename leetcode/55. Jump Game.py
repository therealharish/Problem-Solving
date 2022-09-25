class Solution :
    def canJump (self, nums: List[int]) -> bool:
      dp  = [False]*len(nums)
      dp[-1] = True
      for i in range(len(nums)-2, -1, -1):
        moves = nums[i]
        for j in range(moves):
          if(dp[j] == True):
            dp[i] = True
            break
      if(d[0] == True):
        return True
      else:
        return False
        