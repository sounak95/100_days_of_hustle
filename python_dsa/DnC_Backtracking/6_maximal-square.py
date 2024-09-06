# https://leetcode.com/problems/maximal-square/

class Solution(object):

    def helper(self, mat, i, j, maxi):
        if i>=len(mat) or j>=len(mat[0]):
            return 0

        right = 1 + self.helper(mat, i, j+1, maxi)
        diagonal = 1 +self.helper(mat, i+1, j+1, maxi)
        down =1 + self.helper(mat, i+1, j, maxi)

        if mat[i][j]=='1':
            ans = min(right, min(diagonal, down))
            maxi[0] = max(maxi[0], ans)
            return ans
        else:
            return 0

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxi=[0]
        self.helper(matrix, 0, 0, maxi)
        return maxi[0] * maxi[0]