class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        profit=0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j>i:
                    profit=prices[j]-prices[i]
                max_profit = max(max_profit,profit)
        return max_profit
        