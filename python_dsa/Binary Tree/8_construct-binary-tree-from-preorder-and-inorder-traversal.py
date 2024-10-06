# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def helper(self, preorder, preindex, inorder_start, inorder_end, search_map):
        if preindex[0]>=len(preorder) or inorder_start>inorder_end:
            return None

        pre_index= preindex[0]
        element = preorder[pre_index]

        Node = TreeNode(element)

        position = search_map[element]
        preindex[0]=preindex[0]+1

        Node.left = self.helper(preorder, preindex, inorder_start, position-1, search_map)
        Node.right = self.helper(preorder, preindex, position+1, inorder_end, search_map)

        return Node



    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        search_map= {}

        for i, ele in enumerate(inorder):
            search_map[ele] =i

        preindex=[]
        preindex.append(0)

        return self.helper(preorder, preindex, 0, len(inorder)-1, search_map)


