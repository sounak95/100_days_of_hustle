
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root ==None:
            return None

        if root.val ==p.val:
            return p

        if root.val==q.val:
            return q

        left_ans = self.lowestCommonAncestor(root.left, p, q)
        right_ans = self.lowestCommonAncestor(root.right, p, q)

        if left_ans==None and right_ans==None:
            return None
        elif left_ans!=None and right_ans==None:
            return left_ans
        elif left_ans==None and right_ans!=None:
            return right_ans

        else:
            return root