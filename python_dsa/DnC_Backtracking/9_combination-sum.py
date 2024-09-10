# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def helper(self, candidates, target, index, ans, v):
        if target==0:
            ans.append(list(v))
            return
        if target<0:
            return

        for i in range(index, len(candidates)):
            v.append(candidates[i])
            self.helper(candidates, target-candidates[i], i, ans, v)
            v.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans =[]
        v=[]
        self.helper(candidates, target, 0, ans, v)
        return ans
