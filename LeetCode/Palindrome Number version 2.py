
"""Решение ChatGPT"""


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        original = x
        reverse = 0

        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return original == reverse


x = 121
res = Solution.isPalindrome(x)
print(res)
