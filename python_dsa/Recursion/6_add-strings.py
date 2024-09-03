# https://leetcode.com/problems/add

class Solution(object):

    def helper(self, num1, p1, num2, p2, carry, ans):
        if p1 < 0 and p2 < 0:
            if carry != 0:
                ans.append(carry)
            return ans

        n1 = 0
        n2 = 0

        if p1 >= 0:
            n1 = int(num1[p1])
        if p2 >= 0:
            n2 = int(num2[p2])

        num = n1 + n2 + carry
        digit = num % 10
        carry = num // 10
        ans.append(str(digit))

        return self.helper(num1, p1 - 1, num2, p2 - 1, carry, ans)

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = self.helper(num1, len(num1) - 1, num2, len(num2) - 1, 0, [])
        return "".join(reversed(ans))

print(Solution().addStrings("123", "11"))