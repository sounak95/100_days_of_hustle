# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/


class Solution(object):
    def helper_rec(self, s1, i, s2, j):
        if i ==len(s1):
            cost=0
            for index in range(j, len(s2)):
                cost+= ord(s2[index])
            return cost

        if j == len(s2):
            cost = 0
            for index in range(i, len(s1)):
                cost += ord(s1[index])
            return cost

        if s1[i]==s2[j]:
            return self.helper_rec(s1, i+1, s2, j+1)
        else:
            cost1 = ord(s1[i]) + self.helper_rec(s1, i+1, s2, j)
            cost2 = ord(s2[j]) + self.helper_rec(s1, i, s2, j+1)
            return min(cost1, cost2)



    def minimumDeleteSum_rec(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        return self.helper_rec(s1, 0, s2, 0)

    def helper_mem(self, s1, i, s2, j, dp):
        if i ==len(s1):
            cost=0
            for index in range(j, len(s2)):
                cost+= ord(s2[index])
            return cost

        if j == len(s2):
            cost = 0
            for index in range(i, len(s1)):
                cost += ord(s1[index])
            return cost

        if dp[i][j]!=-1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j]= self.helper_rec(s1, i+1, s2, j+1)
        else:
            cost1 = ord(s1[i]) + self.helper_mem(s1, i+1, s2, j, dp)
            cost2 = ord(s2[j]) + self.helper_mem(s1, i, s2, j+1, dp)
            dp[i][j]= min(cost1, cost2)
        return dp[i][j]



    def minimumDeleteSum_mem(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp=[[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        return self.helper_mem(s1, 0, s2, 0, dp)


    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp=[[-1 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1):
                    cost = 0
                    for index in range(j, len(s2)):
                        cost += ord(s2[index])
                    dp[i][j] = cost
                    continue

                if j == len(s2):
                    cost = 0
                    for index in range(i, len(s1)):
                        cost += ord(s1[index])
                    dp[i][j]= cost
                    continue

                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    cost1 = ord(s1[i]) + dp[i+1][j]
                    cost2 = ord(s2[j]) + dp[i][j+1]
                    dp[i][j] = min(cost1, cost2)


        return dp[0][0]
