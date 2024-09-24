# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution(object):

    def __init__(self):
        self.max_len = 1  # Initialize with 1 because any single character is a palindrome
        self.start = 0  # Index of the starting character of the longest palindrome

    def check_pal_rec(self, s, i, j):
        if i>=j:
            return True

        flag = False
        if s[i]==s[j]:
            flag = self.check_pal_rec(s, i+1, j-1)

        if flag:
            curr_len = j-i+1
            if curr_len>self.max_len:
                self.max_len = curr_len
                self.start = i


    def longestPalindrome_rec(self, s):
        """
        :type s: str
        :rtype: str
        """

        for i in range(len(s)):
            for j in range(i, len(s)):
                self.check_pal_rec(s, i, j)

        return s[self.start: self.start+ self.max_len]

    def check_pal_mem(self, s, i, j, dp):
        if i>=j:
            return True

        if dp[i][j]!=-1:
            return dp[i][j]

        flag = False
        if s[i]==s[j]:
            flag = self.check_pal_mem(s, i+1, j-1, dp)

        dp[i][j]=flag

        if flag:
            curr_len = j - i + 1
            if curr_len > self.max_len:
                self.max_len = curr_len
                self.start = i

        return dp[i][j]


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp=[[-1 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                self.check_pal_mem(s, i, j, dp)

        return s[self.start: self.start+ self.max_len ]
