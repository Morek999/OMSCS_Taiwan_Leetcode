# Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        mini = nums[0]
        mid = float('inf')
        for i in nums:
            if i <= mini:
                mini = i
            else:
                if i > mid:
                    return True
                else:
                    mid = i
        return False


ans = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,5,2,3],
    [5,2,3,4,1]
]
for trails in ans:
    print(Solution().increasingTriplet(trails))