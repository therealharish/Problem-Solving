class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque([])
        ans = []
        for i in range(k):
            if(d and nums[i]<=nums[d[0]]):
                d.appendleft(i)
            elif(d and nums[i]>=nums[d[0]]):
                while(d and nums[i]>=nums[d[0]]):
                    d.popleft()
                d.appendleft(i)
            else:
                d.appendleft(i)
        ans.append(nums[d[-1]])
        for i in range(k, len(nums)):
            if(d and nums[i]<=nums[d[0]]):
                d.appendleft(i)
                if(d[-1]<=(i-k)):
                    d.pop()
            elif(d and nums[i]>=nums[d[0]]):
                while(d and nums[i]>nums[d[0]]):
                    d.popleft()
                if(d and d[-1]<=(i-k)):
                    d.pop()
                d.appendleft(i)
                
            else:
                d.appendleft(i)
            ans.append(nums[d[-1]])
        return ans
        
            
        