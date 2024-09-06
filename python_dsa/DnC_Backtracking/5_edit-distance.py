# https://leetcode.com/problems/edit-distance/description/

class Solution(object):
    def helper(self, word1, word2, i, j):
        if i>=len(word1):
            return len(word2)-j
        if j>=len(word2):
            return len(word1)-i

        if word1[i]==word2[j]:
            return 0 + self.helper(word1, word2, i+1, j+1)
        else:
            option1 = 1+ self.helper(word1, word2, i, j+1) # insert
            option2 = 1+ self.helper(word1, word2, i+1, j) #delete
            option3 = 1+ self.helper(word1, word2, i+1, j+1)
            return min(option1, min(option2, option3))

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.helper(word1, word2, 0, 0)

