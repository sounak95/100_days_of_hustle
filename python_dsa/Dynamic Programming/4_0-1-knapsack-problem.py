# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/

# User function Template for python3

class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def helper_recc(self, W, wt, val, index):
        if index==len(val):
            return 0

        include =0
        if wt[index]<=W:
            include = val[index] + self.helper_recc(W-wt[index], wt, val, index+1)
        exclude = 0 + self.helper_recc(W, wt, val, index+1)

        return max(include, exclude)

    def knapSack_rec(self, W, wt, val):
        return self.helper_recc(W, wt, val, 0)

    def helper_mem(self, W, wt, val, index, dp):
        if index==len(val):
            return 0

        if dp[index][W]!=-1:
            return dp[index][W]

        include =0
        if wt[index]<=W:
            include = val[index] + self.helper_mem(W-wt[index], wt, val, index+1, dp)
        exclude = 0 + self.helper_mem(W, wt, val, index+1, dp)

        dp[index][W] = max(include, exclude)
        return dp[index][W]

    def knapSack_mem(self, W, wt, val):
        dp = [[-1 for _ in range(W+1)] for _ in range(len(val))]
        return self.helper_mem(W, wt, val, 0, dp)

    def knapSack(self, W, wt, val):
        n= len(val)
        dp = [[0 for _ in range(W + 1)] for _ in range(n+1)]

        for w in range(W+1):
            dp[n][w]=0

        for index in range(n-1, -1, -1):
            for w in range(W+1):
                include = 0
                if wt[index] <= w:
                    include = val[index] + dp[index + 1][w - wt[index]]
                exclude = 0 + dp[index + 1][w]

                dp[index][w] = max(include, exclude)

        return dp[0][W]


# code here


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends