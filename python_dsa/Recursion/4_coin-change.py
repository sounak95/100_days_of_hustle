# https://leetcode.com/problems/coin-change/description/

class Solution(object):

    def helper(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        mini = float('inf')

        for coin in coins:
            mini = min(mini, 1 + self.helper(coins, amount - coin))

        return mini

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = self.helper(coins, amount)
        if ans == float('inf'):
            return -1
        return ans