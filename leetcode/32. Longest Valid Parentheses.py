class Solution:
    def longestValidParentheses(self, s: str) -> int:
      st=[-1]
      ans = 0
      for i,j in enumerate(s):
        if(j=="("):
          st.append(i)
        elif(j==")"):
            st.pop()
            if(st):
              ans = max(ans, i-(st[-1]))
            else:
              st.append(i)
      return ans
          