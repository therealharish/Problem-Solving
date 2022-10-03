class Solutions:
    def scoreOfParentheses(self, s: str) -> int:
        s = "("+s+")"
        st = []
        for i in s:
            if(i==')'):
                if(st[-1]=='('):
                    st.pop()
                    st.append(1)
                else:
                    ans = 0
                    while(st[-1]!="("):
                        ans+=st.pop()
                    st.pop()
                    st.append(2*ans)
            else:
                st.append(i)
        return st[-1]//2

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for i in s:
            if(i==')'):
                if(st[-1]=='('):
                    st.pop()
                    st.append(1)
                else:
                    ans = 0
                    while(st[-1]!="("):
                        ans+=st.pop()
                    st.pop()
                    st.append(2*ans)
            else:
                st.append(i)
        if(len(st)==1):
            return st[-1]
        else:
            return sum(st)
                    