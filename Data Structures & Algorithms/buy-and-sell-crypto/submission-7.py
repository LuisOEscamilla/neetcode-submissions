class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 1:
            return profit
        #Sliding window
        start = 0
        end = 1
        while end < len(prices):
            if prices[end] > prices[start]:
                currProfit = prices[end] - prices[start]
                profit = max(currProfit, profit)
                
            else:
                start = end
            end += 1
        return profit   