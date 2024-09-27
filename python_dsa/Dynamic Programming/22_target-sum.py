# https://leetcode.com/problems/target-sum/
class Solution(object):

    def solve_rec(self,nums, target, i):
        if i==len(nums):
            return 1 if target==0 else 0

        plus = self.solve_rec(nums, target-nums[i], i+1)
        minus = self.solve_rec(nums, target+ nums[i], i+1)

        return plus + minus


    def findTargetSumWays_rec(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.solve_rec(nums, target, 0)

    def solve_mem(self,nums, target, i, dp):
        if i==len(nums):
            return 1 if target==0 else 0

        if (i,target) in dp:
            return dp[(i,target)]

        plus = self.solve_mem(nums, target-nums[i], i+1, dp)
        minus = self.solve_mem(nums, target+ nums[i], i+1, dp)

        dp[(i,target)] =  plus + minus

        return dp[(i,target)]


    def findTargetSumWays_mem(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp={}
        return self.solve_mem(nums, target, 0, dp)

    def findTargetSumWays(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        total = sum(nums)

        dp[(len(nums), 0)] =1

        for i in range(len(nums)-1, -1, -1):
            for tgt in range(-total, total+1):
                plus =  dp.get((i+1, (tgt-nums[i])), 0)
                minus = dp.get((i+1, (tgt+nums[i])), 0)

                dp[(i, tgt)] = plus + minus

        return dp.get((0,target), 0)
