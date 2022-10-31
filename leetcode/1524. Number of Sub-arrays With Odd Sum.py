class Solution1:
    def numOfSubarrays(self, nums: List[int]) -> int:
#         addedd the same logic as subarray sum divisible by k
      k=2
      arr = [0]*(len(nums)+1)
      for i in range(len(nums)):
        arr[i+1] = (arr[i]+nums[i])%k
      print(arr)

      bucket = [0]*k
      for i in arr:
        bucket[i]+=1
    
      ans = 0
      for i in bucket:
        if(i>1):
            ans+= math.comb(i, 2)
      l  = len(nums)
    
      total = (l*(l+1))//2
      ans = total - ans
            
      return ans  % (10**9 + 7)

class Solution:
    def numOfSubarrays(self, nums: List[int]) -> int:
        odd = 0
        even = 0
        count = 0
        mod = 10**9 + 7
        for i in nums:
            if(i&1):
                temp = odd
                odd = even+1
                even = temp
                count+=odd
            else:
                even+=1
                count+=odd
        return count%mod
                