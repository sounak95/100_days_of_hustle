from typing import List

class Solution:
    def helper(self, i, j, m, n, vis, out, ans):
        if i==n-1 and j==n-1:
            ans.append(out)
            return

        if i-1>=0 and vis[i-1][j]==0 and m[i-1][j]==1:
            vis[i-1][j]=1
            self.helper(i-1, j, m, n, vis, out+"U", ans)
            vis[i - 1][j] = 0

        if i + 1 < n and vis[i + 1][j] == 0 and m[i + 1][j] == 1:
            vis[i + 1][j] = 1
            self.helper(i + 1, j, m, n, vis, out + "D", ans)
            vis[i + 1][j] = 0

        if j-1 >=0 and vis[i][j-1] == 0 and m[i][j-1] == 1:
            vis[i][j-1] = 1
            self.helper(i, j-1, m, n, vis, out + "L", ans)
            vis[i][j - 1] = 0

        if j+1 < n and vis[i][j+1] == 0 and m[i][j+1] == 1:
            vis[i][j+1] = 1
            self.helper(i, j+1, m, n, vis, out + "R", ans)
            vis[i][j + 1] = 0

    def findPath(self, m):
        # code here
        n=len(m)
        rows, cols = (n, n)
        vis = [[0 for _ in range(cols)] for _ in range(rows)]
        ans=[]
        if m[0][0]==1:
            vis[0][0] = 1 #missed this
            self.helper(0,0,m,n,vis,"", ans)
        return ans



#{
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends