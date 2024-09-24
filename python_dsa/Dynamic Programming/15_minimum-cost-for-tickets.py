# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution(object):
    def helper_rec(self, days, costs, i):
        if i>=len(days):
            return 0

        cost0 = costs[0] + self.helper_rec(days, costs, i+1)

        pass_end_day = days[i] + 7 -1
        j=i
        while(j<len(days) and days[j]<=pass_end_day):
            j+=1

        cost7 = costs[1] + self.helper_rec(days, costs, j)

        pass_end_day = days[i] + 30 - 1
        j = i
        while (j < len(days) and days[j] <= pass_end_day):
            j += 1

        cost30 = costs[2] + self.helper_rec(days, costs, j)

        return min(cost0, cost7, cost30)



    def mincostTickets_rec(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        return  self.helper_rec(days, costs, 0)


    def helper_mem(self, days, costs, i, dp):
        if i>=len(days):
            return 0

        if dp[i]!=-1:
            return dp[i]

        cost0 = costs[0] + self.helper_rec(days, costs, i+1)

        pass_end_day = days[i] + 7 -1
        j=i
        while(j<len(days) and days[j]<=pass_end_day):
            j+=1

        cost7 = costs[1] + self.helper_rec(days, costs, j)

        pass_end_day = days[i] + 30 - 1
        j = i
        while (j < len(days) and days[j] <= pass_end_day):
            j += 1

        cost30 = costs[2] + self.helper_rec(days, costs, j)

        dp[i] = min(cost0, cost7, cost30)
        return dp[i]



    def mincostTickets_mem(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp= [-1 for _ in range(len(days)+1)]
        return  self.helper_mem(days, costs, 0, dp)

    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp= [-1 for _ in range(len(days)+1)]
        n=len(days)
        dp[n] =0
        for i in range(n-1, -1, -1):
            cost0 = costs[0] + dp[i+1]

            pass_end_day = days[i] + 7 - 1
            j = i
            while (j < len(days) and days[j] <= pass_end_day):
                j += 1

            cost7 = costs[1] + dp[j]

            pass_end_day = days[i] + 30 - 1
            j = i
            while (j < len(days) and days[j] <= pass_end_day):
                j += 1

            cost30 = costs[2] + dp[j]

            dp[i] = min(cost0, cost7, cost30)
        
        return  dp[0]
