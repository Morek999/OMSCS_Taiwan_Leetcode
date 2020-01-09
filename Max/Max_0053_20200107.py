# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        tmp_sum = max_sum = -float('inf')
        for i in nums:
            tmp_sum = max(i, tmp_sum + i)
            max_sum = max(max_sum, tmp_sum)
            # print(f'{tmp_sum}: {max_sum}')
        return max_sum

ans = [
    [-2],
    [-2,1,-3,4,-1,2,1,-5,4]
]
for trails in ans:
    print(Solution().maxSubArray(trails))
