#memoization
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {}
        if(obstacleGrid[m-1][n-1]==1):
            return 0
        def recur(r, c):
            if(r>m-1 or c>n-1):
                dp[(r, c)] = 0
                return 0
            if(obstacleGrid[r][c]==1):
                dp[(r, c)] = 0
                return 0
            if(r==m-1 and c==n-1):
                dp[(r, c)] = 1
                return 1
            if((r,c) in dp):
                return dp[(r,c)]
            dp[(r,c)] = recur(r+1, c) + recur(r, c+1)
            return dp[(r, c)]
        
        ans = recur(0, 0)
        return ans
        
        
# tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if(obstacleGrid[0][0] or obstacleGrid[m-1][n-1]):
            return 0
        obstacleGrid[0][0] = 1
        for r in range(m):
            for c in range(n):
                if(r==0 and c==0):
                    continue
                elif(obstacleGrid[r][c]==1):
                    obstacleGrid[r][c] = 0
                elif(r==0 and c!=0):
                    obstacleGrid[r][c] = obstacleGrid[r][c-1]
                elif(r!=0 and c==0):
                    obstacleGrid[r][c] = obstacleGrid[r-1][c]
                else:
                    obstacleGrid[r][c] = obstacleGrid[r][c-1]+obstacleGrid[r-1][c]
        return obstacleGrid[m-1][n-1]
                
 