# https://leetcode.com/problems/path-sum/description/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root==None:
            return False

        targetSum-=root.val

        if root.left==None and root.right==None:
            if targetSum==0:
                return True
            return False

        left_path = self.hasPathSum(root.left, targetSum)
        right_path = self.hasPathSum(root.right, targetSum)

        return left_path or right_path
