class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 1:
            return profit
        #Sliding window
        start = 0
        end = 1
        while end < len(prices):
            currProfit = prices[end] - prices[start]
            if currProfit > profit:
                profit = currProfit
            if prices[end] < prices[start]:
                start += 1
            else:
                end += 1
        return profit   