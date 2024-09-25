# https://leetcode.com/problems/house-robber-iii/


    # Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def solve_rec(self, root):
        if not root:
            return 0

        donotinclude = 0

        include = root.val
        if root.left:
            include += self.solve_rec(root.left.left) + self.solve_rec(root.left.right)
        if root.right:
            include += self.solve_rec(root.right.left) + self.solve_rec(root.right.right)

        donotinclude = self.solve_rec(root.left) + self.solve_rec(root.right)
        return max(include, donotinclude)

    def rob_rec(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.solve_rec(root)

    def solve_mem(self, root, dp):
        if not root:
            return 0

        if root in dp:
            return dp[root]

        include = root.val
        if root.left:
            include += self.solve_mem(root.left.left, dp) + self.solve_mem(root.left.right, dp)
        if root.right:
            include += self.solve_mem(root.right.left, dp) + self.solve_mem(root.right.right, dp)

        donotinclude = self.solve_mem(root.left, dp) + self.solve_mem(root.right, dp)
        dp[root] = max(include, donotinclude)

        return dp[root]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dp = {}
        return self.solve_mem(root, dp)
