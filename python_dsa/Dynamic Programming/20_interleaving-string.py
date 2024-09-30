'''
helper_rec(s1 = "ab", s2 = "cd", s3 = "abcd", i = 0, j = 0, k = 0)

Decision: s1[0] == s3[0] ('a' == 'a')
    |
    v
helper_rec(s1 = "ab", s2 = "cd", s3 = "abcd", i = 1, j = 0, k = 1)

Decision: s1[1] == s3[1] ('b' == 'b')
    |
    v
helper_rec(s1 = "ab", s2 = "cd", s3 = "abcd", i = 2, j = 0, k = 2)

Decision: i == len(s1), so move to check s2

Decision: s2[0] == s3[2] ('c' == 'c')
    |
    v
helper_rec(s1 = "ab", s2 = "cd", s3 = "abcd", i = 2, j = 1, k = 3)

Decision: s2[1] == s3[3] ('d' == 'd')
    |
    v
helper_rec(s1 = "ab", s2 = "cd", s3 = "abcd", i = 2, j = 2, k = 4)

Base Case: i == len(s1), j == len(s2), and k == len(s3)
Return True

'''

# https://leetcode.com/problems/interleaving-string/description/

class Solution(object):

    def helper_rec(self, s1, s2, s3, i, j, k):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        flag = False
        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            flag = flag or self.helper_rec(s1, s2, s3, i + 1, j, k + 1)

        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            flag = flag or self.helper_rec(s1, s2, s3, i, j + 1, k + 1)

        return flag

    def isInterleave_rec(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        return self.helper_rec(s1, s2, s3, 0, 0, 0)

    def helper_mem(self, s1, s2, s3, i, j, k, dp):
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True

        if dp[i][j][k]!=-1:
            return dp[i][j][k]

        flag = False
        if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
            flag = flag or self.helper_mem(s1, s2, s3, i + 1, j, k + 1, dp)

        if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
            flag = flag or self.helper_mem(s1, s2, s3, i, j + 1, k + 1, dp)

        dp[i][j][k] = flag

        return dp[i][j][k]

    def isInterleave_mem(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp=[[[-1 for _ in range(len(s3)+1)]for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        return self.helper_mem(s1, s2, s3, 0, 0, 0, dp)


    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp=[[[-1 for _ in range(len(s3)+1)]for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                for k in range(len(s3), -1, -1):
                    if i == len(s1) and j == len(s2) and k == len(s3):
                        dp[i][j][k] = True
                        continue

                    flag = False
                    if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                        flag =  dp[i+1][j][k+1]

                    if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                        flag = flag or dp[i][j+1][k+1]

                    dp[i][j][k] = flag

        return dp[0][0][0]

