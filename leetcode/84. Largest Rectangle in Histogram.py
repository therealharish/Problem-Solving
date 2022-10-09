class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
#       function to find next smallest element to right
        def nser(heights):
            m = len(heights)
            st = []
            ans = [m]*len(heights)
            for i in range(len(heights)-1, -1, -1):
                curr = heights[i]
                while(st and curr <= heights[st[-1]]):
                    st.pop()
                if(st):
                    ans[i] = st[-1]
                st.append(i)
            return ans
        
#       function to find next smallest element to left
        def nsel(heights):
            st = []
            ans = [-1]*len(heights)
            for i in range(len(heights)):
                curr = heights[i]
                while(st and curr <= heights[st[-1]]):
                    st.pop()
                if(st):
                    ans[i] = st[-1]
                st.append(i)
            return ans
        
        arrSER = nser(heights)
        arrSEL = nsel(heights)
        print(arrSEL, arrSER)
        m = 0
        for i in range(len(heights)):
            left = arrSEL[i]
            right = arrSER[i]
#             right - left - 1 ensures that the actual element that we could have gone till was actually our index+1 or -1 in those cases
            m = max(m, (right-left-1)*heights[i])
        return m
        
        
                    
                                