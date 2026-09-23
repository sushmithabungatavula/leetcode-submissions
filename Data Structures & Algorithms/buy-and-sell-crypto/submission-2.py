class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_profit=0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                max_profit= max(max_profit,profit)
            else:
                left=right
            # left+=1
            right+=1
        return max_profit











        # max_profit=0
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if j>i:
        #             profit=prices[j]-prices[i]
        #         max_profit = max(max_profit,profit)
        # return max_profit


        