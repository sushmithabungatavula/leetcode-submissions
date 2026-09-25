class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit= prices[j]-prices[i]
        #         max_profit= max(max_profit, profit)
        # return max_profit

        max_profit=0
        left=0
        n=len(prices)
        for right in range(n):
            if prices[right]<=prices[left]:
                left=right
            else:
                profit=prices[right]-prices[left]
                max_profit=max(max_profit,profit)
            # left+=1
            # right-=1
        return max_profit











































        # left=0
        # right=1
        # max_profit=0
        # while right<len(prices):
        #     if prices[right]>prices[left]:
        #         profit=prices[right]-prices[left]
        #         max_profit= max(max_profit,profit)
        #     else:
        #         left=right
        #     # left+=1
        #     right+=1
        # return max_profit


        # max_profit=0
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if j>i:
        #             profit=prices[j]-prices[i]
        #         max_profit = max(max_profit,profit)
        # return max_profit


        