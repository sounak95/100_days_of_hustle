# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.d=0

    def height(self, root):
        if not root:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        curr_d = lh + rh
        self.d = max(self.d, curr_d)

        return max(lh,rh)+1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.height(root)
        return self.d

