class Solution:

    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        mLeft = height[0]
        mRight = height[n - 1]
        
        left = 1
        right = n-2
        
        total = 0
        
        while left <= right:
            if mLeft < mRight:
                total += max(mLeft - height[left], 0)
                mLeft = max(mLeft, height[left])
                left += 1
            else:
                total += max(mRight - height[right], 0)
                mRight = max(mRight, height[right])
                right -= 1

        return total