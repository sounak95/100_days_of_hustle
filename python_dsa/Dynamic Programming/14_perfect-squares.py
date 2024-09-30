# https://leetcode.com/problems/perfect-squares/description/
# no. of ways
import math
class Solution(object):
    def helper_rec(self, n):
        if n==0:
            return 0

        if n<0:
            return float('inf')
        ans = float('inf')
        for i in range(1, int(math.sqrt(n))+1):
            ans = min(ans, 1+ self.helper_rec(n-(i*i)))

        return ans

    def numSquares_rec(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper_rec(n)


    def helper_mem(self, n, dp):
        if n==0:
            return 0

        if n<0:
            return float('inf')

        if dp[n]!=-1:
            return dp[n]

        ans = float('inf')
        for i in range(1, int(math.sqrt(n))+1):
            ans = min(ans, 1+ self.helper_rec(n-(i*i)))

        dp[n] = ans
        return dp[n]

    def numSquares_mem(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1 for _ in range(n+1)]
        return self.helper_mem(n, dp)

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1 for _ in range(n+1)]

        for num in range(n+1):
            if num==0:
                dp[num]=0
                continue
            ans = float('inf')
            for i in range(1, int(math.sqrt(num)) + 1):
                # important
                if num-(i*i)>=0:
                    ans = min(ans, 1 + dp[num-(i*i)])

            dp[num] = ans

        return dp[n]


        return self.helper_mem(n, dp)



