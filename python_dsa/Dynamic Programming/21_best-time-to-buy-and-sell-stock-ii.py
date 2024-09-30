# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# include exclude

class Solution(object):
    def helper_rec(self, prices, i, buy):
        if i>=len(prices):
            return 0

        if buy:
            buy_it_profit = -prices[i] + self.helper_rec(prices, i+1, 0)
            skip_it_profit = self.helper_rec(prices, i+1, buy)
            profit = max(buy_it_profit, skip_it_profit)
        else:
            sell_it_profit =prices[i] + self.helper_rec(prices, i+1, 1)
            skip_it_profit = self.helper_rec(prices, i+1, buy)
            profit = max(sell_it_profit, skip_it_profit)

        return profit


    def maxProfit_rec(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        return self.helper_rec(prices, 0, 1)

    def helper_mem(self, prices, i, buy, dp):
        if i>=len(prices):
            return 0

        if dp[i][buy]!=-1:
            return dp[i][buy]

        if buy:
            buy_it_profit = -prices[i] + self.helper_mem(prices, i+1, 0, dp)
            skip_it_profit = self.helper_mem(prices, i+1, buy, dp)
            profit = max(buy_it_profit, skip_it_profit)
        else:
            sell_it_profit =prices[i] + self.helper_mem(prices, i+1, 1, dp)
            skip_it_profit = self.helper_mem(prices, i+1, buy, dp)
            profit = max(sell_it_profit, skip_it_profit)

        dp[i][buy] = profit
        return dp[i][buy]

    def maxProfit_mem(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[[-1 for _ in range(2)] for _ in range(len(prices)+1)]

        return self.helper_mem(prices, 0, 1, dp)


    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[[0 for _ in range(2)] for _ in range(len(prices)+2)]

        for i in range(len(prices), -1 , -1):
            for buy in range(1, -1, -1):
                if i >= len(prices):
                    dp[i][buy] = 0
                    continue

                if buy:
                    # note i+1 hence range(len(prices)+2)
                    buy_it_profit = -prices[i] +dp[i+1][0]
                    skip_it_profit = dp[i+1][buy]
                    profit = max(buy_it_profit, skip_it_profit)
                else:
                    sell_it_profit = prices[i] + dp[i+1][1]
                    skip_it_profit = dp[i+1][buy]
                    profit = max(sell_it_profit, skip_it_profit)

                dp[i][buy] = profit


        return dp[0][1]


