class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0;
        r = len(l)-1
        area = 0;
        while(l<r):
            temp = (r-l)*max(height(r)), height(l)
            if(temp > area):
                area = temp
                
            