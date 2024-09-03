# https://leetcode.com/problems/perfect-squares/
import math

# https://leetcode.com/problems/perfect-squares/

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n<0:
            return float('inf')

        ans =float('inf')
        for i in range(1, int(math.sqrt(n))+1):
            perf_sq = i*i
            num_perf_sq = 1 + self.numSquares(n-perf_sq)
            ans = min(ans, num_perf_sq)

        return ans

print(Solution().numSquares(12))

