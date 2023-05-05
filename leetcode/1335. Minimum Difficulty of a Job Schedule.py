class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        l = len(jobDifficulty)
        dp = {}
        def solve(i, d):
            if(d==1):
                return max(jobDifficulty[i:])
            if((i, d) in dp):
                return dp[(i, d)]

            maxD = float('-inf')
            res = float('inf')
            for j in range(i, l - d + 1):
              maxD = max(maxD, jobDifficulty[j])
              res = min(res, maxD + solve(j+1, d-1))

            dp[(i, d)] = res
            return res
        if(l < d):
            return -1
        return solve(0, d)
      
                
                