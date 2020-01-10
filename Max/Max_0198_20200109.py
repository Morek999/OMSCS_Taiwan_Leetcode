""" 
198. House Robber
https://leetcode.com/problems/house-robber/
Time complexity: O(n)
Space complexity: O(1)
Solution: Since 2 adj robbery are not allowed, we need 2 variables to keep tracking
    CURRent maximum value and the PREVious maximum value. To decide whether to rob
    ith house, we need to compare (PREV + ith house) and CURR and moving the 2
    pointers 1-step forward.
 """

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        curr = prev = 0
        for i in nums:
            temp = curr
            curr = max(prev + i, curr)
            prev = temp
            # print(f'{i}: {curr} _ {prev}')
        return curr
        

ans = [
    [1,2,3,1],
    [2,7,9,3,1]
]
for trails in ans:
    print(Solution().rob(trails))
