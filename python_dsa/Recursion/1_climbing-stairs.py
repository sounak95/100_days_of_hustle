# https://leetcode.com/problems/climbing-stairs/description

#how many ways

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        if n==0:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)


