# in notes 1 pg 7
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      left = 0
      right = len(nums)-1
      i = len(nums)-1
      ans = [0]*len(nums)
      while(left<=right):
        lsquare = nums[left]**2
        rsquare = nums[right]**2
        if(lsquare>rsquare):
          ans[i] = lsquare
          left+=1
        elif(rsquare>lsquare):
          ans[i] = rsquare
          right-=1
        else:
          ans[i] = rsquare
          right-=1
        i-=1
      return ans

# channa sir, 3 approaches

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums
      
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums)-1
        ans  = [0]*len(nums)
        x = len(nums)-1
        while(low<=high):
            if(nums[low]**2>nums[high]**2):
                ans[x] = nums[low]**2
                x-=1
                low+=1
            else:
                ans[x] = nums[high]**2
                x-=1
                high-=1
        return ans
                
        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        pos = len(nums)
        for i in range(len(nums)):
            if(nums[i]>=0):
                pos = i
                break
        neg = pos-1
        # print(neg, pos)
        while(neg>-1 and pos<len(nums)):
            if(nums[neg]**2<nums[pos]**2):
                ans.append(nums[neg]**2)
                neg-=1
            else:
                ans.append(nums[pos]**2)
                pos+=1
            # print(ans)
        while(neg>-1):
            ans.append(nums[neg]**2)
            neg-=1
        while(pos<len(nums)):
            ans.append(nums[pos]**2)
            pos+=1
        
        return ans
                
            
        
            
        
      
          
        
        
          
        
        
          
        
        