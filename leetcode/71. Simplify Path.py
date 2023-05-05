class Solution:
    def simplifyPath(self, path: str) -> str:
        d = path.split("/")
        st = []
        for i in d:
            if(i == '.' or i== ''):
                continue
            elif(i==".."):
                if st:
                    st.pop()
            else:
                st.append(i)
        ans = "/" + "/".join(st)
        return ans
                
        