# https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def helper_rec(self, text1, i, text2, j):
        if i >= len(text1):
            return 0

        if j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + self.helper_rec(text1, i + 1, text2, j + 1)
        else:
            return max(self.helper_rec(text1, i + 1, text2, j), self.helper_rec(text1, i, text2, j + 1))

    def longestCommonSubsequence_rec(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.helper_rec(text1, 0, text2, 0)

    def helper_mem(self, text1, i, text2, j, dp):
        if i >= len(text1):
            return 0

        if j >= len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.helper_mem(text1, i + 1, text2, j + 1, dp)
        else:
            dp[i][j] = max(self.helper_mem(text1, i + 1, text2, j, dp), self.helper_mem(text1, i, text2, j + 1, dp))

        return dp[i][j]

    def longestCommonSubsequence_mem(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper_mem(text1, 0, text2, 0, dp)

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]













