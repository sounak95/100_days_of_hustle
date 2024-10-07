# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def helper(self, p, q):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if p and q:
            return p.val ==q.val and self.helper(p.left, q.right) and self.helper(p.right, q.left)

        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root.left, root.right)
