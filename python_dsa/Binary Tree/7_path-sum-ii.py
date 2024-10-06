# https://leetcode.com/problems/path-sum-ii/description/

class Solution(object):

    def helper(self, root, targetSum, result, l1):
        if root == None:
            return

        targetSum-=root.val
        l1.append(root.val)
        if root.left==None and root.right==None:
            if targetSum==0:
                result.append(l1)
            return

        self.helper(root.left, targetSum, result, l1.copy())
        self.helper(root.right, targetSum, result, l1.copy())


    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result=[]
        l1=[]
        self.helper(root, targetSum, result, l1.copy())
        return result
