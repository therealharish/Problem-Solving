class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        ans = [float('inf')]*(len(nums)-1)
        ans.append(0)
        for i in range(len(nums)-2, -1, -1):
            limit = i+nums[i]+1 
#             limit is the limit till which the j loop will run, it starts from i +1
            m = float('inf')
            for j in range(i+1, min(l, limit)):
                m = min(ans[j]+1, m)
                if(m==1):
                    break
            ans[i] = m
        return ans[0]
                
            