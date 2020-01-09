# Majority Element
# https://leetcode.com/problems/majority-element/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        holding = {}
        for i in nums:
            if i in holding:
                holding[i] += 1
            else:
                holding[i] = 1
            if holding[i] > (len(nums) / 2):
                return i

print(Solution().majorityElement([3,2,3]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))
print(Solution().majorityElement([1]))
