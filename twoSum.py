'''
Two Sum:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
to target. You may assume that each input would have exactly one solution, and you may not use the same element
twice. You can return the answer in any order.

Time Complexity: O(n)

Space Complexity: O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevNums:
                return [prevNums[diff], index]
            prevNums[value] = index