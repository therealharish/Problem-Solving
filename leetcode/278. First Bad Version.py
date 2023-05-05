# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution1:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        ans = -1
        if(isBadVersion(1)==True):
            return 1
        while(low<=high):
            mid = (low+high)//2
            print(low, mid, high, n)
            if(mid<n and isBadVersion(mid)==False and isBadVersion(mid+1)==True):
                ans = mid+1
                break
            elif(isBadVersion(mid)==False):
                low = mid+1
            else:
                high = mid-1
        return ans
                
            
# we make sure the answer is always in the range
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        ans = -1
        while(low<high):
            mid = (low+high)//2
            if(isBadVersion(mid)):
                high = mid
            else:
                low = mid+1
        return low