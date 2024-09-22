# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# 00:10:40.40
class Solution(object):

    def helper_rec(self, s, e):
        if s >= e:
            return 0

        ans = float('inf')
        for i in range(s, e):
            ans = min(ans, i + max(self.helper_rec(s, i - 1), self.helper_rec(i + 1, e)))

        return ans

    def getMoneyAmount_rec(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper_rec(1, n)

    def helper_mem(self, s, e, dp):
        if s >= e:
            return 0

        if dp[s][e]!=-1:
            return dp[s][e]

        ans = float('inf')
        for i in range(s, e):
            ans = min(ans, i + max(self.helper_mem(s, i - 1, dp), self.helper_mem(i + 1, e, dp)))

        dp[s][e]= ans

        return dp[s][e]

    def getMoneyAmount_mem(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]
        return self.helper_mem(1, n, dp)

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[-1 for _ in range(n+1)]for _ in range(n+1)]

        for s in range(n, 0 , -1):
            for e in range(1, n+1):
                if s>=e:
                    dp[s][e]=0
                ans = float('inf')
                for i in range(s, e):
                    ans = min(ans, i + max(dp[s][i-1], dp[i+1][e]))
                    dp[s][e]= ans

        return dp[1][n]
