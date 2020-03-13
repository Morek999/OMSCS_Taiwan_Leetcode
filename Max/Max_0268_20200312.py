""" 
268. Missing Number
https://leetcode.com/problems/missing-number/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = len(nums)
        for n, i in enumerate(nums):
            miss ^= i ^ n
        return miss

ans = [
    [3,0,1],      
    [9,6,4,2,3,5,7,0,1]       
]
for trails in ans:
    print(Solution().missingNumber(trails))
