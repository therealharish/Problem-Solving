class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        sq = [[0 for _ in range(col)] for _ in range(row)]
        m = 0
        for i in range(row):
            for j in range(col):
                sq[i][j] = int(matrix[i][j])
                m = max(m, sq[i][j])


        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == "1" and matrix[i-1][j-1] =="1" and matrix[i-1][j] =="1" and matrix[i][j-1]=="1":
                    sq[i][j] = min(sq[i-1][j-1], sq[i-1][j], sq[i][j-1]) + 1
                    m = max(m, sq[i][j])
        return m*m 
                    
    
        
        