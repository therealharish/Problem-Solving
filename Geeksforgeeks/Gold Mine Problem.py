class Solution:
    def maxGold(self, n, m, M):
        # m,n are cols and rows respectively ugh
        if n == 1:
            return sum(M[0])
        table = [[0 for j in range(m)] for i in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    table[j][i] = M[j][i]
                elif j == 0 and j+1<n:
                    table[j][i] = max(table[j][i-1], table[j+1][i-1]) + M[j][i]
                elif(j==n-1 and j-1>=0):
                    table[j][i] = max(table[j-1][i-1], table[j][i-1]) + M[j][i]
                else:
                    table[j][i] = max(table[j-1][i-1], table[j][i-1], table[j+1][i-1]) + M[j][i]
        maximum = float("-inf")
        for i in range(n):
            maximum = max(maximum, table[i][-1])
        return maximum
