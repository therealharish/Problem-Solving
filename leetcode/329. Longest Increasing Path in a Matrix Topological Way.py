# dp solution
class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        row, col = len(matrix), len(matrix[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        dp = {}
        def dfs(i, j, prev):
            if i < 0 or i >= row or j < 0 or j >= col or  matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 0
            for r, c in direction:
                res = max(res, dfs(i+r, j+c, matrix[i][j]))
            dp[(i, j)] = res+1
            return dp[(i, j)]

        
        ans = 0
        for i in range(row):
            for j in range(col):
                ans = max(ans, dfs(i, j, -float('inf')))
        return ans
            
# topological sorting solution
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        inDegree = [[0 for _ in range(col)] for _ in range(row)]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i in range(row):
            for j in range(col):
                for r, c in direction:
                    if i+r < 0 or i+r >= row or j+c < 0 or j+c >= col:
                        continue
                    if matrix[i+r][j+c] > matrix[i][j]:
                        inDegree[i][j] += 1
                
        queue = deque()        
        for i in range(row):
            for j in range(col):
                if inDegree[i][j] == 0:
                    queue.append((i, j))
                    
        print(queue)
        
        count = 0
        while(queue):
            count += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for i in range(len(direction)):
                    x, y = r + direction[i][0], c + direction[i][1]
                    if x < 0 or x >= row or y < 0 or y >= col:
                        continue
                    if matrix[x][y] > matrix[r][c]:
                        inDegree[x][y] -= 1
                        if inDegree[x][y] == 0:
                            queue.append((x, y))
                            
        return count
            
                
        