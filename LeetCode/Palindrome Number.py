"""Мое решение"""


class Solution:
    @classmethod
    def isPalindrome(cls, x: int) -> bool:
        if x < 0:
            return False

        ranks = cls.get_ranks(x)
        while ranks > 0:
            if x // (10**ranks) != x % 10:
                return False
            x = (x % (10**ranks)) // 10
            ranks -= 2

        return True

    @staticmethod
    def get_ranks(number: int) -> int:
        k = 0
        while number != 0:
            number = number // 10
            k += 1
        return k - 1


x = -1
res = Solution.isPalindrome(x)
print(res)
