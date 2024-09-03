# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        if target<0:
            return 0
        if n==0 and target==0:
            return 1
        if n==0 or target==0:
            return 0
        ans=0
        for i in range(1, k+1):
            ans+=self.numRollsToTarget(n-1, k, target-i)

        return ans

print(Solution().numRollsToTarget(2, 6, 7))
