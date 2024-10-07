# https://leetcode.com/problems/balanced-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def __init__(self):
        self.is_balanced = True

    def height(self, root):
        if not root:
            return 0

        lh= self.height(root.left)
        rh= self.height(root.right)

        if self.is_balanced and abs(lh-rh)>1:
            self.is_balanced = False

        return max(lh, rh)+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.height(root)
        return self.is_balanced
