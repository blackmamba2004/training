"""Мое решение"""

class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        complements = {}

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in complements.keys():
                return [i, complements[complement]]
            
            complements[nums[i]] = i

        return []


nums = [7, 9, 16, 3, 0]
print(Solution.twoSum(nums, 9))
