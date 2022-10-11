class SolutionS:
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
                

class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if(l==1):
            return 0
        end = nums[0]
        maxR = nums[0]
        jump = 1
        for i in range(len(nums)-1):
#             we don't check the last index because if we reached the last index then we have reached the last already right? It's simple, why will we update it then?
            maxR = max(maxR, i+nums[i])
            if(i==end):
                end = maxR
                jump+=1
        return jump