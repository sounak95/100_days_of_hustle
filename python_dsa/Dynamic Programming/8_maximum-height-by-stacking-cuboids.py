# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
# 00:14:59.70
class Solution(object):
    def check(self, cuboids, curr_ind, prev_ind):
        if cuboids[curr_ind][0] >= cuboids[prev_ind][0] and cuboids[curr_ind][1] >= cuboids[prev_ind][1] and \
                cuboids[curr_ind][2] >= cuboids[prev_ind][2]:
            return True
        return False

    def check_rev(self, cuboids, curr_ind, prev_ind):
        if cuboids[curr_ind][0] <= cuboids[prev_ind][0] and cuboids[curr_ind][1] <= cuboids[prev_ind][1] and \
                cuboids[curr_ind][2] <= cuboids[prev_ind][2]:
            return True
        return False

    def helper_rec(self, cuboids, curr_ind, prev_ind):
        if curr_ind == len(cuboids):
            return 0

        include = 0
        if prev_ind == -1 or self.check_rev(cuboids, curr_ind, prev_ind):
            include = cuboids[curr_ind][2] + self.helper_rec(cuboids, curr_ind + 1, curr_ind)
        exclude = self.helper_rec(cuboids, curr_ind + 1, prev_ind)
        return max(include, exclude)

    def maxHeight_rec(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort(reverse=True)
        return self.helper_rec(cuboids, 0, -1)

    def helper_mem(self, cuboids, curr_ind, prev_ind, dp):
        if curr_ind == len(cuboids):
            return 0

        if dp[curr_ind][prev_ind+1]!=-1:
            return dp[curr_ind][prev_ind+1]

        include = 0
        if prev_ind == -1 or self.check(cuboids, curr_ind, prev_ind):
            include = cuboids[curr_ind][2] + self.helper_mem(cuboids, curr_ind + 1, curr_ind, dp)
        exclude = self.helper_mem(cuboids, curr_ind + 1, prev_ind, dp)

        dp[curr_ind][prev_ind+1] =  max(include, exclude)

        return dp[curr_ind][prev_ind+1]

    def maxHeight_mem(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        n= len(cuboids)
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.helper_mem(cuboids, 0, -1, dp)


    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        n= len(cuboids)
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort(reverse= True)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for curr_ind in range(n-1, -1, -1):
            for prev_ind in range(curr_ind-1, -2, -1):
                include = 0
                if prev_ind == -1 or self.check_rev(cuboids, curr_ind, prev_ind):
                    include = cuboids[curr_ind][2] + dp[curr_ind + 1][curr_ind+1]
                exclude = dp[curr_ind+1][prev_ind+1]

                dp[curr_ind][prev_ind + 1] = max(include, exclude)

        return dp[0][0]


