# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def helper(self, root):
        if root==None:
            return 0

        left_height= self.helper(root.left)
        right_height = self.helper(root.right)

        return max(left_height, right_height)+1


    def maxDepth(self, root):
        return self.helper(root)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        current_node_ans= abs(left_height-right_height)<=1

        left_ans = self.isBalanced(root.left)
        right_ans = self.isBalanced(root.right)

        return current_node_ans and left_ans and right_ans
