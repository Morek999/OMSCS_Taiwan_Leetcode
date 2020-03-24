""" 
136. Single Number
https://leetcode.com/problems/single-number/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

ans = [
    [2,2,1], # 1
    [4,1,2,1,2]   # 4
]
for trails in ans:
    print(Solution().singleNumber(trails))
