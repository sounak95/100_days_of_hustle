

class Solution:

    def helper(self, root, level, levelData):
        if not root:
            return

        if level not in levelData:
            levelData[level] = []
        levelData[level].append(root.data)

        self.helper(root.left, level+1, levelData)
        self.helper(root.right, level, levelData)


    def diagonal(self,root):
        levelData = {}
        self.helper(root, 0, levelData)

        level=0
        res=[]
        while(level in levelData):
            res.extend(levelData[level])
            level+=1

        return res





