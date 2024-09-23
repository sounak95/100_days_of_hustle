# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
MOD = 10**9 + 7
# 00:19:04.80
class Solution(object):

    def helper_rec(self, n, k, target, dice_count , sum):
        if dice_count==n and sum ==target:
            return 1

        if dice_count==n and sum!=target:
            return 0

        if dice_count!=n and sum==target:
            return 0

        ans =0
        for face in range(1, k+1):
            if sum + face<=target:
                ans += self.helper_rec(n, k, target, dice_count+1 , sum+face)% MOD
        return ans

    def numRollsToTarget_rec(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """

        return self.helper_rec(n, k, target, 0, 0)

    def helper_mem(self, n, k, target, dice_count , sum, dp):
        if dice_count==n and sum ==target:
            return 1

        if dice_count==n and sum!=target:
            return 0

        if dice_count!=n and sum==target:
            return 0

        if dp[dice_count][sum]!=-1:
            return dp[dice_count][sum]

        ans =0
        for face in range(1, k+1):
            if sum + face<=target:
                ans += self.helper_mem(n, k, target, dice_count+1 , sum+face, dp) % MOD
        dp[dice_count][sum] =  ans % MOD

        return dp[dice_count][sum]

    def numRollsToTarget_mem(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for _ in range(target+1)]for _ in range(n+1)]
        return self.helper_mem(n, k, target, 0, 0, dp)


    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for _ in range(target+1)]for _ in range(n+1)]

        for dice_count in range(n, -1, -1):
            for sum in range(target, -1, -1):
                if dice_count == n and sum == target:
                    dp[dice_count][sum] = 1
                    continue

                if dice_count == n and sum != target:
                    dp[dice_count][sum] = 0
                    continue

                if dice_count != n and sum == target:
                    dp[dice_count][sum] = 0
                    continue

                ans = 0
                for face in range(1, k + 1):
                    if sum + face <= target:
                        ans += dp[dice_count + 1][ sum + face] % MOD
                dp[dice_count][sum] = ans % MOD

        return dp[0][0]





print(Solution().numRollsToTarget(2, 6, 7))



