# https://leetcode.com/problems/house-robber/description/

class Solution(object):

    def helper(self, nums, index):
        if index >= len(nums):
            return 0

        option1 = nums[index] + self.helper(nums, index+2)
        option2 = 0 + self.helper(nums, index + 1)

        return max(option1, option2)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.helper(nums, 0)
