class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = []
        def solve(i, sum):
            if i>=len(cost):
                ans.append(sum)
                return 0
            solve(2*i+1, sum+cost[i])
            solve(2*i+2, sum+cost[i])
        solve(0, 0)
        res = 0
        print(ans)
        
        #function to return min operations needed to make all array elements equal
        def ops(ans):
            
        
