# https://leetcode.com/problems/coin-change/description/
# num of coins

class Solution(object):
    def helper_rec(self,coins, amount):
        if amount==0:
            return 0

        ans = float('inf')
        for coin in coins:
            if amount-coin>=0:
                ans = min(ans, 1 + self.helper_rec(coins, amount-coin))
        return ans



    def coinChange_rec(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        ans = self.helper_rec(coins, amount)
        if ans == float('inf'):
            return -1
        return ans

    def helper_mem(self, coins, amount, dp):
        if amount == 0:
            return 0

        if dp[amount]!=-1:
            return dp[amount]

        ans = float('inf')
        for coin in coins:
            if amount - coin >= 0:
                ans = min(ans, 1 + self.helper_mem(coins, amount - coin, dp))
        dp[amount] = ans
        return dp[amount]

    def coinChange_mem(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount+1)
        if amount==0:
            return 0
        ans = self.helper_mem(coins, amount, dp)
        if ans == float('inf'):
            return -1
        return ans

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        dp = [0] * (amount + 1)

        for amt in range(1, amount+1):
            ans = float('inf')
            for coin in coins:
                if amt-coin>=0:
                    ans = min(ans , 1+ dp[amt-coin])
            dp[amt] = ans
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]



