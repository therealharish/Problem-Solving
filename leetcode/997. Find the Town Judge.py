class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        possibility = [True] * n
        counts = [0] * n
        
        for i in trust:
            counts[i[1] - 1] += 1
            possibility[i[0] - 1] = False
        
        for i in range(n):
            if possibility[i] and (counts[i] == n - 1):
                return i + 1
        
        return -1