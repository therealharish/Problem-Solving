class Solution:
    def maxArea(self, height: List[int]) -> int:
      l = 0;
      r = len(height)-1
      area = 0;
      while(l<r):
          temp = (r-l)*min(height[r], height[l])
          if(temp > area):
              area = temp
          if(height[l]<height[r]):
            l+=1
          else:
            r-=1
      return area
                
            