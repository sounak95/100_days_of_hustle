# https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1


# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None



# Function to return a list containing elements of left view of the binary tree.

def helper(root, level, res):
    if root is None:
        return

    if level==len(res):
        res.append(root.data)

    helper(root.left, level+1, res)
    helper(root.right, level+1, res)

def LeftView(root):
    res=[]
    helper(root, 0, res)
    return res


# code here
