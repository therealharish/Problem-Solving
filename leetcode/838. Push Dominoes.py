class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        # for i in range(len(dominoes)):
        #     if(dominoes[i]=="."):
        #         if(i>0 and i<len(dominoes)-1 and dominoes[i-1]=="R" and dominoes[i+1]=="L"):
        #             continue
        #         elif(i>0 and dominoes[i-1]=="R"):
        #             dominoes[i] = "R"
        #         elif(i< len(dominoes)-1 and dominoes[i+1]=="L"):
        #             dominoes[i] = "L"
        # return "".join(dominoes)
        st = deque([])
        for i in range(len(dominoes)):
            if(dominoes[i]!="."):
                st.append(i)
    
        while(st):
            i = st.popleft()
            if(dominoes[i]=="L"):
                if(i>0 and dominoes[i-1]=="."):
                    dominoes[i-1] = "L"
                    st.append(i-1)
            if(dominoes[i]=="R"):
                if(i<len(dominoes)-2 and dominoes[i+1]=="." and dominoes[i+2]=="L"):
                    st.popleft()
                elif(i<len(dominoes)-1 and dominoes[i+1]=="."):
                    dominoes[i+1] = "R"
                    st.append(i+1)
        return "".join(dominoes)
            
                
                    
                    