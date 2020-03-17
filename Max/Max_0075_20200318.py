""" 
75. Sort Colors
https://leetcode.com/problems/sort-colors/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = curr = 0
        p2 = len(nums) - 1
        while p2 >= curr:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
        
        # nums.sort()
        

ans = [
    [2,0,2,1,1,0]   # [0,0,1,1,2,2]
]
for trails in ans:
    print(Solution().maxProduct(trails))
