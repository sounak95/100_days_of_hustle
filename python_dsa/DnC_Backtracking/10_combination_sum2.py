# https://leetcode.com/problems/combination-sum-ii/description/

class Solution(object):
    def helper(self, candidates, target, index,ans, v ):
        if target==0:
            ans.append(list(v))
            return

        if target<0:
            return

        for i in range(index, len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            v.append(candidates[i])
            self.helper(candidates, target-candidates[i], i+1, ans, v)
            v.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        v=[]
        self.helper(sorted(candidates), target, 0, ans, v)
        return ans
