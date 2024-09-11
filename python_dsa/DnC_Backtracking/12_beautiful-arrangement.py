

# https://leetcode.com/problems/beautiful-arrangement/description/


class Solution(object):
    def helper(self, v, n, currNum, ans):
        if currNum==n+1:
            ans[0]+=1
            return

        for i in range(1, n+1):
            if v[i]==0 and (i%currNum==0 or currNum%i==0):
                v[i] = currNum
                self.helper(v, n, currNum+1, ans)
                v[i]=0

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[0]
        v=[0] * (n+1)
        self.helper(v, n,1, ans)
        return ans
