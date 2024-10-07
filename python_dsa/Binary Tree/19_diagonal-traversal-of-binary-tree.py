
class Solution:

    def diagonal(self ,root):
        q=[]
        q.append(root)
        ans=[]

        while(len(q)!=0):
            temp= q.pop( 0)
            while(temp):
                if temp.left:
                    q.append(temp.left)

                ans.append(temp.data)

                temp = temp.right

        return ans






