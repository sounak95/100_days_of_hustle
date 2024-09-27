# https://leetcode.com/problems/ones-and-zeroes/

class Solution(object):
    def solve_rec(self, numStrs, m, n, i):
        if i == len(numStrs):
            return 0

        include = 0
        exclude = self.solve_rec(numStrs, m, n, i + 1)
        zeros, ones = numStrs[i]
        if m - zeros >= 0 and n - ones >= 0:
            include = 1 + self.solve_rec(numStrs, m - zeros, n - ones, i + 1)

        return max(include, exclude)

    def getNumStrs(self, strs):
        numStrs = []
        for s in strs:
            numStrs.append([s.count("0"), s.count("1")])
        return numStrs

    def findMaxForm_rec(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        numsStrs = self.getNumStrs(strs)
        return self.solve_rec(numsStrs, m, n, 0)

    def solve_mem(self, numStrs, m, n, i, dp):
        if i == len(numStrs):
            return 0

        if dp[i][m][n]!=-1:
            return dp[i][m][n]

        include = 0
        exclude = self.solve_mem(numStrs, m, n, i + 1, dp)
        zeros, ones = numStrs[i]
        if m - zeros >= 0 and n - ones >= 0:
            include = 1 + self.solve_mem(numStrs, m - zeros, n - ones, i + 1, dp)

        dp[i][m][n]=  max(include, exclude)
        return dp[i][m][n]


    def findMaxForm_mem(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        numsStrs = self.getNumStrs(strs)

        dp=[[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]
        return self.solve_mem(numsStrs, m, n, 0, dp)

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        numStrs = self.getNumStrs(strs)
        dp=[[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len(strs)+1)]

        for i in range(len(strs), -1,-1):
            for ind_m in range(m+1):
                for ind_n in range(n+1):
                    if i == len(strs):
                        dp[i][ind_m][ind_n]=0
                        continue
                    include = 0
                    exclude = dp[i+1][ind_m][ind_n]
                    zeros, ones = numStrs[i]
                    if ind_m - zeros >= 0 and ind_n - ones >= 0:
                        include = 1 + dp[i+1][ind_m-zeros][ind_n-ones]

                    dp[i][ind_m][ind_n] = max(include, exclude)

        return dp[0][m][n]


