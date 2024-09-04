

# https://leetcode.com/problems/house-robber-ii/description/

class Solution(object):
    def helper(self, s, e, nums):
        if s>e:
            return 0

        option1 = nums[s] + self.helper(s+2, e, nums)
        option2 = 0 + self.helper(s + 1, e, nums)
        return max(option1, option2)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        if n==1:
            return nums[0]
        return max(self.helper(0,n-2, nums), self.helper(1, n-1, nums))
