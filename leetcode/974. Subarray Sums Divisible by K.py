class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      arr = [0]*(len(nums)+1)
      for i in range(len(nums)):
        arr[i+1] = (arr[i]+nums[i])%k
      print(arr)

      bucket = [0]*k
      for i in arr:
        bucket[i]+=1
      print(bucket)
    
      ans = 0
      for i in bucket:
        if(i>1):
            ans+= math.comb(i, 2)
      return ans