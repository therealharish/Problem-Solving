#     used the same logic as 283 in notes p1 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = p2 = 0
        while(p2<len(nums)):
            if(nums[p2]==val):
                p2+=1
            else:
                if(p1!=p2):
                    nums[p2], nums[p1] = nums[p1], nums[p2]
                p2+=1
                p1+=1
        return p1
    
