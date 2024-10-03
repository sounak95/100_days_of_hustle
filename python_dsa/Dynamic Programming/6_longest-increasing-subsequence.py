# https://leetcode.com/problems/longest-increasing-subsequence/
# include exclude

class Solution(object):
    def helper_rec(self, nums, curr_ind, prev_ind):
        if curr_ind == len(nums):
            return 0

        include = 0
        if prev_ind == -1 or nums[curr_ind] > nums[prev_ind]:
            include = 1 + self.helper_rec(nums, curr_ind + 1, curr_ind)

        exclude = self.helper_rec(nums, curr_ind + 1, prev_ind)

        return max(include, exclude)

    def lengthOfLIS_rec(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper_rec(nums, 0, -1)

    def helper_mem(self, nums, curr_ind, prev_ind, dp):
        if curr_ind == len(nums):
            return 0

        # index shifting
        if dp[curr_ind][prev_ind + 1] != -1:
            return dp[curr_ind][prev_ind + 1]

        include = 0
        if prev_ind == -1 or nums[curr_ind] > nums[prev_ind]:
            include = 1 + self.helper_mem(nums, curr_ind + 1, curr_ind, dp)

        exclude = self.helper_mem(nums, curr_ind + 1, prev_ind, dp)

        dp[curr_ind][prev_ind + 1] = max(include, exclude)

        # index shifting
        return dp[curr_ind][prev_ind + 1]

    def lengthOfLIS_mem(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return self.helper_mem(nums, 0, -1, dp)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for curr_ind in range(n-1, -1, -1):
            # important
            for prev_ind in range(curr_ind-1, -2, -1):
                include = 0
                if prev_ind == -1 or nums[curr_ind] > nums[prev_ind]:
                    # index shifting
                    include = 1 + dp[curr_ind + 1][curr_ind+1]
                # index shifting
                exclude = dp[curr_ind + 1][prev_ind+1]
                # index shifting
                dp[curr_ind][prev_ind + 1] = max(include, exclude)

        return dp[0][0]







