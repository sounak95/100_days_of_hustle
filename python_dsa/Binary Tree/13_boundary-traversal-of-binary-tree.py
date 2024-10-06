# https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

class Solution:

    def left_boundery(self, root, res):
        if root is None:
            return

        if root.left==None and root.right==None:
            return

        res.append(root.data)

        if root.left:
            self.left_boundery(root.left, res)
        else:
            self.left_boundery(root.right, res)

    def right_boundery(self, root, res):
        if root is None:
            return

        if root.left == None and root.right == None:
            return

        if root.right:
            self.right_boundery(root.right, res)
        else:
            self.right_boundery(root.left, res)

        res.append(root.data)

    def leaf_boundery(self, root, res):
        if root is None:
            return

        if root.left == None and root.right == None:
            res.append(root.data)

        # Collect leaves from left subtree first
        self.leaf_boundery(root.left, res)
        # Then collect leaves from the right subtree
        self.leaf_boundery(root.right, res)



    def printBoundaryView(self, root):
        # Code here

        res=[]
        res.append(root.data)

        self.left_boundery(root.left, res)
        self.leaf_boundery(root.left, res)
        self.leaf_boundery(root.right, res)
        self.right_boundery(root.right, res)

        return res

