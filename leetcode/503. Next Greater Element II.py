class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
      st = nums.copy()
      ans = [-1]*len(nums)
      for i in range(len(nums)-1, -1, -1):
        curr = nums[i]
        while(st and curr>=st[-1]):
          st.pop()
        if(st):
          ans[i] = st[-1]
        st.append(curr)
      return ans