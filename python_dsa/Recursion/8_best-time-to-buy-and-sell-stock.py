# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def helper(self, prices, min_price, max_profit, i):
        if i>=len(prices):
            return max_profit

        min_price = min(prices[i], min_price)
        profit = prices[i] - min_price
        max_profit = max(profit, max_profit)
        return self.helper(prices, min_price, max_profit, i+1)


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.helper(prices, float('inf'), 0, 0)
