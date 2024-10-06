# https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        q=[]
        q.append([root,0])
        topview={}

        while(len(q)!=0):
            front_ele, hd = q.pop(0)

            if hd not in topview:
                topview[hd] = front_ele.data

            if front_ele.left:
                q.append([front_ele.left, hd-1])

            if front_ele.right:
                q.append([front_ele.right, hd+1])

        res=[]
        for key in sorted(topview.keys()):
            res.append(topview[key])

        return res






# code here