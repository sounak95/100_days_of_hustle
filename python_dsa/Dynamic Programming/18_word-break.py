# https://leetcode.com/problems/word-break/description/

class Solution(object):
    def check(self, word, wordDict):
        return word in wordDict

    def helper_rec(self, s, wordDict, start):
        if start ==len(s):
            return True

        word=""
        flag = False
        for i in range(start, len(s)):
            word+=s[i]
            if self.check(word, wordDict):
                flag = flag or self.helper_rec(s, wordDict, i+1)

        return flag


    def wordBreak_rec(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.helper_rec(s, wordDict, 0)


    def helper_mem(self, s, wordDict, start, dp):
        if start ==len(s):
            return True

        if dp[start]!=-1:
            return dp[start]

        word=""
        flag = False
        for i in range(start, len(s)):
            word+=s[i]
            if self.check(word, wordDict):
                flag = flag or self.helper_rec(s, wordDict, i+1)

        dp[start] = flag

        return dp[start]


    def wordBreak_mem(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[-1 for _ in range(len(s)+1)]
        return self.helper_mem(s, wordDict, 0,dp)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[-1 for _ in range(n+1)]

        for start in range(n,-1, -1 ):
            if start == n:
                dp[start]=True
                continue
            word = ""
            flag = False
            for i in range(start, n):
                word += s[i]
                if self.check(word, wordDict):
                    flag = flag or dp[i+1]

            dp[start] = flag

        return dp[0]
