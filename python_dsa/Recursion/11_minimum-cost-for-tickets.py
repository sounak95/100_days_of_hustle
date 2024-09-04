# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution(object):

    def helper(self, days, cost, i):
        if i>=len(days):
            return 0

        cost1 = cost[0] + self.helper(days, cost, i+1)

        pass_end_day= days[i] + 7 -1
        j=i
        while(j<len(days) and days[j]<= pass_end_day):
            j+=1
        cost7 = cost[1] + self.helper(days, cost, j)

        pass_end_day = days[i] + 30-1
        j=i
        while(j<len(days) and days[j]<=pass_end_day):
            j+=1
        cost30 = cost[2] + self.helper(days, cost, j)

        return min(cost1,cost7, cost30 )



    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """

        return self.helper(days, costs, 0)
