class Solution:
    def nextLargerElement(self,arr,n):
        st = []
        ans = [-1]*len(arr)
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            while(st and curr>=st[-1]):
                st.pop()
            if(st):
                ans[i] = st[-1]
            st.append(curr)
        return ans