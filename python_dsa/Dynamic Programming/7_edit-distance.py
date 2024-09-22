# https://leetcode.com/problems/edit-distance/description/

# 00:11:21.43
class Solution(object):

    def helper_rec(self, word1, i, word2, j):
        if i==len(word1):
            return len(word2)-j

        if j==len(word2):
            return len(word1)-i

        if word1[i]==word2[j]:
            return 0 + self.helper_rec(word1, i+1, word2, j+1)
        else:
            replace = 1 + self.helper_rec(word1, i+1, word2, j+1)
            delete = 1 + self.helper_rec(word1, i + 1, word2, j )
            add = 1 + self.helper_rec(word1, i, word2, j+1)

            return min(replace, delete, add)


    def minDistance_mem(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.helper_rec(word1, 0, word2, 0)

    def helper_mem(self, word1, i, word2, j, dp):
        if i==len(word1):
            return len(word2)-j

        if j==len(word2):
            return len(word1)-i

        if dp[i][j]!=-1:
            return dp[i][j]

        if word1[i]==word2[j]:
            dp[i][j] = 0 + self.helper_mem(word1, i+1, word2, j+1, dp)
        else:
            replace = 1 + self.helper_mem(word1, i+1, word2, j+1, dp)
            delete = 1 + self.helper_mem(word1, i + 1, word2, j, dp)
            add = 1 + self.helper_mem(word1, i, word2, j+1, dp)

            dp[i][j] = min(replace, delete, add)

        return dp[i][j]

    def minDistance_mem(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        return self.helper_mem(word1, 0, word2, 0, dp)

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2)-j

        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1)-i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = 0 + dp[i+1][j+1]
                else:
                    replace = 1 + dp[i+1][j+1]
                    delete = 1 + dp[i+1][j]
                    add = 1 + dp[i][j+1]

                    dp[i][j] = min(replace, delete, add)
        return dp[0][0]








