# https://leetcode.com/problems/partition-equal-subset-sum/
# 00:13:05.24

# include exclude
class Solution(object):
    def helper_rec(self, nums, index, sum, target):
        if index>=len(nums):
            return 0

        if sum ==target:
            return 1

        if sum>target:
            return 0
        include = 0
        if sum + nums[index] <= target:
            include = self.helper_rec(nums, index+1, sum+ nums[index], target)
        exclude = self.helper_rec(nums, index+1, sum, target)

        return include or exclude


    def canPartition_rec(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target=0
        for num in nums:
            target+=num

        if target%2!=0:
            return False

        target=target//2

        return self.helper_rec(nums, 0, 0, target)

    def helper_mem(self, nums, index, sum, target, dp):
        if index>=len(nums):
            return 0

        if sum ==target:
            return 1

        if sum>target:
            return 0

        if dp[index][sum]!=-1:
            return dp[index][sum]
        include =0
        if sum + nums[index] <= target:
            include = self.helper_mem(nums, index+1, sum+ nums[index], target, dp)
        exclude = self.helper_mem(nums, index+1, sum, target, dp)

        dp[index][sum] = include or exclude
        return dp[index][sum]


    def canPartition_mem(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n= len(nums)
        target=0
        for num in nums:
            target+=num

        if target%2!=0:
            return False

        target=target//2
        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]
        return self.helper_mem(nums, 0, 0, target, dp)

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n= len(nums)
        target=0
        for num in nums:
            target+=num

        if target%2!=0:
            return False

        target=target//2
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

        for index in range(n-1, -1, -1):
            for sum in range(target, -1, -1):
                if sum == target:
                    dp[index][sum] = 1
                    continue
                if sum>target:
                    dp[index][sum]=0
                    continue
                include =0
                # missed this
                if sum+ nums[index]<=target:
                    include =dp[index + 1][sum + nums[index]]
                exclude = dp[index + 1][sum]
                dp[index][sum] = include or exclude


        return dp[0][0]


