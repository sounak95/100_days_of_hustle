# https://leetcode.com/problems/russian-doll-envelopes/

# include exclude
class Solution(object):

    def check(self, envelopes, curr_ind, prev_ind):
        if envelopes[curr_ind][0] < envelopes[prev_ind][0] and envelopes[curr_ind][1] < envelopes[prev_ind][1] :
            return True
        return False

    def maxEnvelopes(self, envelopes):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        envelopes.sort(reverse = True)

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for curr_ind in range(n - 1, -1, -1):
            for prev_ind in range(curr_ind - 1, -2, -1):
                include = 0
                if prev_ind == -1 or self.check(envelopes, curr_ind, prev_ind):
                    include = 1 + dp[curr_ind + 1][curr_ind + 1]
                exclude = dp[curr_ind + 1][prev_ind + 1]

                dp[curr_ind][prev_ind + 1] = max(include, exclude)

        return dp[0][0]

