class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recur(ans, curr):
            if(curr[1]==0 and curr[2]==0):
                ans.append(curr[0])
                return
            elif(curr[1]>0 and curr[2]>curr[1]):
                 recur(ans, [curr[0]+"(", curr[1]-1, curr[2]])
                 recur(ans, [curr[0]+")", curr[1], curr[2]-1])
            elif(curr[1]>0 and curr[2]<=curr[1]):
                 recur(ans, [curr[0]+"(", curr[1]-1, curr[2]])
            elif(curr[1]==0 and curr[2]>0):
                recur(ans, [curr[0]+")", curr[1], curr[2]-1])
        recur(ans, ["", n, n])
        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def solve(open, close, s):
            
            if open == 0 and close == 0:
                ans.append(s)
                
            elif open == 0 and close > 0:
                solve(open, close-1, s+")")
        
            elif open == close:
                solve(open-1, close, s+"(")
            
            elif open < close:
                solve(open-1, close, s+"(")
                solve(open, close-1, s+")")
                
        solve(n, n, "")
                