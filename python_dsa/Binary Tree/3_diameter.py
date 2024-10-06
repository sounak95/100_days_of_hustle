
# User function Template for python3



class Solution:

    def helper(self, root):
        if root==None:
            return 0

        left_height= self.helper(root.left)
        right_height = self.helper(root.right)

        return max(left_height, right_height)+1


    def maxDepth(self, root):
        return self.helper(root)

    # Function to return the diameter of a Binary Tree.
    def diameter(self ,root):
        if root==None:
            return 0

        option1 = self.diameter(root.left)
        option2 = self.diameter(root.right)
        option3 = self.maxDepth(root.left) + self.maxDepth(root.right)+1

        return max(option1, max(option2, option3))

