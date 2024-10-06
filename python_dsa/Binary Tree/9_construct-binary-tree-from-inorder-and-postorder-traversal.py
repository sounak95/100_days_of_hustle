# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def helper(self, postindex, inorder_start, inorder_end, inorder, postorder, search_map):
        if postindex[0]>=len(postorder) or inorder_start>inorder_end:
            return None

        post_index= postindex[0]
        element =postorder[post_index]

        Node = TreeNode(element)
        position  = search_map[element]

        postindex[0]-=1
        Node.right = self.helper(postindex, position+1, inorder_end, inorder, postorder, search_map)
        Node.left  = self.helper(postindex, inorder_start, position-1, inorder, postorder, search_map)

        return Node


    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        search_map={}
        for i, ele in enumerate(inorder):
            search_map[ele] =i

        #important
        postindex=[len(postorder)-1]
        return self.helper(postindex, 0, len(inorder)-1, inorder, postorder, search_map)
