class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        st = []
        ans = [-1]*len(a)
        for i in range(len(a)):
            curr = a[i]
            while(st and curr>=st[-1][1]):
                st.pop()
            if(st):
                ans[i] = st[-1][0]
            st.append((i, a[i]))
        
        for i in range(len(ans)):
            ans[i] = i-ans[i]
        
        return ans