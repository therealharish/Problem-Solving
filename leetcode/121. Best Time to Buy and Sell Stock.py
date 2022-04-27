class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      mi = max(prices)
      profit = 0
      for i in range(len(prices)):
        mi = min(prices[i], mi)
        profit = max(profit, prices[i]-mi)
      return profit
        