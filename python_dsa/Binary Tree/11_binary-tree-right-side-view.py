# https://leetcode.com/problems/binary-tree-right-side-view/

class Solution(object):

    def helper(self, root, level, res):
        if root is None:
            return

        if level==len(res):
            res.append(root.val)

        self.helper(root.right, level+1, res)
        self.helper(root.left, level + 1, res)


    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]

        self.helper(root, 0, res)
        return res
