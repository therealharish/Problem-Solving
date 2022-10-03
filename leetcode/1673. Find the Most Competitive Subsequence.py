
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st = []
        canDelete = len(nums)-k
        if(canDelete == 0):
            return nums
        for i in range(len(nums)):
            curr = nums[i]
            while(st and curr<st[-1] and canDelete):
                canDelete-=1
                st.pop(-1)
            st.append(curr)
        return st[0:k]
            