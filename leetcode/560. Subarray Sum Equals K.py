class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      sum=0;
      count=0;
      for i in range(len(nums)):
        for j in range(i, len(nums)):
          sum+=nums[j]   
          if(sum==k):
            count+=1;
            sum=0
            break;
          elif(sum>k):
            sum=0
            break
        sum=0
      return count
      
        