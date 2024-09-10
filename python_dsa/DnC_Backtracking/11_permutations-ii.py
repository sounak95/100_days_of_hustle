# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def helper(self, nums, ans, index):
        if index>=len(nums):
            ans.append(nums[:])
        visited = set()
        for i in range(index, len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            self.helper(nums, ans, index+1)
            nums[index], nums[i] = nums[i], nums[index]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        self.helper(nums, ans, 0)
        return ans

