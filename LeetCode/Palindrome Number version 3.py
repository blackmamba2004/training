"""Решение крутого чувака с LeetCode"""

class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return x == reverse or x == reverse // 10


x = 10
res = Solution.isPalindrome(x)
print(res)
