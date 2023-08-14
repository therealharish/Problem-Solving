class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def solve(amount):
            
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            res = 0
            for i in coins:
                res += solve(amount - i)
            return res
        
        return solve(amount)