class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(l, start):
            if start == len(l):
                ans.append(l.copy())
                return 
            for i in range(start, len(l)):
                l[start], l[i] = l[i], l[start]
                solve(l, start+1)
                l[start], l[i] = l[i], l[start]
        solve(nums, 0)  
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def solve(nums):
            ans = []
            if len(nums) == 1:
                ans.append(nums[:])
            
            for i in range(len(nums)):
                n = nums.pop(0)
                perm = solve(nums)
                
                for j in perm:
                    j.append(n)
                ans.extend(perm)
                nums.append(n)

            return ans
    
        return solve(nums)