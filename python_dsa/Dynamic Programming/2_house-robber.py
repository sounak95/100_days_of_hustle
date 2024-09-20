# https://leetcode.com/problems/house-robber/description/

# include exclude

class Solution(object):
    def helper_rec(self, nums, index):
        if index>=len(nums):
            return 0

        include = nums[index] + self.helper(nums, index+2)
        exclude = 0 + self.helper(nums, index+1)

        return max(include, exclude)

    def rob_rec(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper_rec(nums, 0)

    def helper_mem(self, nums,index, dp):
        if index>=len(nums):
            return 0

        if dp[index]!=-1:
            return dp[index]

        include = nums[index] + self.helper_mem(nums, index+2, dp)
        exclude = 0 + self.helper_mem(nums, index+1, dp)
        dp[index]= max(include, exclude)

        return dp[index]

    def rob_mem(self, nums):
        dp = [-1] * len(nums)
        return self.helper_mem(nums, 0, dp)


    def rob(self, nums):
        n=len(nums)
        dp = [-1] * n
        dp[n-1] = nums[n-1]

        for index in range(n-2, -1, -1):
            if index+2<n:
                include = nums[index] + dp[index+2]
            else:
                include = nums[index]
            exclude = 0 + dp[index+1]
            dp[index] = max(include, exclude)

        return dp[0]



