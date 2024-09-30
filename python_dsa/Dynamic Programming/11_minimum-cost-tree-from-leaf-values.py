# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/description/
# range s--> e partition
class Solution(object):

    def helper_rec(self, s, e, maxi):
        if s>=e:
            return 0
        ans = float('inf')
        # important its s--> e and not e+1
        for i in range(s, e):
            ans= min(ans, maxi[(s, i)] * maxi[(i+1, e)] + self.helper_rec(s, i, maxi) + self.helper_rec(i+1, e, maxi))

        return ans

    # 00:10:39.99
    def mctFromLeafValues_rec(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = {}
        n= len(arr)
        for i in range(n):
            maxi[(i,i)] = arr[i]
            for j in range(i+1, n):
                maxi[(i,j)] = max(arr[j], maxi[(i, j-1)])

        return self.helper_rec(0, n-1, maxi)

    def helper_mem(self, s, e, maxi, dp):
        if s>=e:
            return 0
        ans = float('inf')

        if dp[s][e]!=-1:
            return dp[s][e]

        # important its s--> e and not e+1
        for i in range(s, e):
            ans= min(ans, maxi[(s, i)] * maxi[(i+1, e)] + self.helper_mem(s, i, maxi, dp) + self.helper_mem(i+1, e, maxi, dp))

        dp[s][e] =ans

        return dp[s][e]

    def mctFromLeafValues_mem(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = {}
        n= len(arr)
        for i in range(n):
            maxi[(i,i)] = arr[i]
            for j in range(i+1, n):
                maxi[(i,j)] = max(arr[j], maxi[(i, j-1)])

        dp = [[-1 for _ in range(n)] for _ in range(n)]

        return self.helper_mem(0, n-1, maxi, dp)

    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxi = {}
        n= len(arr)
        for i in range(n):
            maxi[(i,i)] = arr[i]
            for j in range(i+1, n):
                maxi[(i,j)] = max(arr[j], maxi[(i, j-1)])

        print(maxi)
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        for s in range(n-1, -1, -1):
           for e in range(0, n):
               if s >= e:
                   dp[s][e] = 0
                   continue
               ans = float('inf')
               for i in range(s, e):
                   ans = min(ans,maxi[(s, i)] * maxi[(i + 1, e)] + dp[s][i] + dp[i+1][e])
               dp[s][e] = ans

        return dp[0][n-1]

print(Solution().mctFromLeafValues([6,2,4]))







