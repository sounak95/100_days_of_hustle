
# https://leetcode.com/problems/maximum-subarray/description/

class Solution(object):
    def helper(self, nums, s, e):
        if s==e:
            return nums[s]

        mid = s+ (e-s)//2

        left_max = self.helper(nums, s , mid)
        right_max=  self.helper(nums, mid+1, e)

        left_border_max = float('-inf')
        right_border_max = float('-inf')
        left_border_sum =0
        right_border_sum = 0

        for i in range(mid, s-1, -1):
            left_border_sum += nums[i]
            left_border_max = max(left_border_max, left_border_sum)

        for i in range(mid+1, e+1):
            right_border_sum += nums[i]
            right_border_max = max(right_border_max, right_border_sum)

        cross_border_sum = left_border_max+ right_border_max

        return max(cross_border_sum, max(right_max, left_max))


    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)

