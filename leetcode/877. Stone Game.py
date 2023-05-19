class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def f1(i, j):
            if i > j:
                return 0
            else:
                return max(piles[i]+f2(i+1, j), f2(i, j-1)+piles[j])
        
        def f2(i, j):
            if i > j:
                return float('inf')
            else:
                return min(f1(i+1, j), f1(i, j-1))

        alice = f1(0, len(piles)-1)
        bob = sum(piles) - alice
        if alice > bob:
            return True
        else:
            return False
        
#tabulation
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dp = [[0 for i in range(len(piles))] for j in range(len(piles))]
        for i in range(len(piles)-1, -1, -1):
            for j in range(len(piles)):
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        alice = dp[0][len(piles)-1]
        if alice > 0:
            return True
        return False