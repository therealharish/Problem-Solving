class Solution1:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        memo = {}
        def recur(i):
            if i>=len(stoneValue):
                return 0
    
            one = float("-inf")
            two = float("-inf")
            three = float("-inf")
            if i in memo:
                return memo[i]

            one = stoneValue[i] - recur(i+1)
            if i+1 < len(stoneValue):
                two = stoneValue[i] + stoneValue[i+1] - recur(i+2)
            if i+2 < len(stoneValue):
                three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - recur(i+3)

            memo[i] = max(one, two, three)
            return memo[i]
            
        
        ans = recur(0)
        if ans == 0:
            return "Tie"
        elif(ans > 0):
            return "Alice"
        else:
            return "Bob"

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @cache
        def f1(i):
            if i>=len(stoneValue):
                return 0
            one, two, three = -float('inf'), -float('inf'), -float('inf')

            one = stoneValue[i] + f2(i+1)
            if i+1 < len(stoneValue):
                two = stoneValue[i] + stoneValue[i+1] + f2(i+2)
            if i+2 < len(stoneValue):
                three = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] + f2(i+3)
            return max(one, two, three)
        
        @cache
        def f2(i):
            if i >= len(stoneValue):
                return 0
            return min(f1(i+1), f1(i+2), f1(i+3))
        

        bestAlice = f1(0)
        # print(bestAlice)
        total = sum(stoneValue)
        bestBob = total - bestAlice

        if bestBob == bestAlice:
            return "Tie"
        elif bestBob > bestAlice:
            return "Bob"
        else:
            return "Alice"