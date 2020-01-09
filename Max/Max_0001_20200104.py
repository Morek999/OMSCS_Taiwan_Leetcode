# Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holding = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k not in holding:
                holding[nums[i]] = i
            else:
                return [holding[k], i]
            

print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
