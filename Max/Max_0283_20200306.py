""" 
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt = None
        for i in range(len(nums)):
            if (nums[i] != 0) and (pt is not None):
                nums[pt] = nums[i]
                pt += 1
                nums[i] = 0
            elif (nums[i] == 0) and (pt is None):
                pt = i
            print(f'{nums}: pt={pt}, i={i}')
        

ans = [
    [0,1,0,3,12],
    [2,1]
]
for trails in ans:
    print(Solution().moveZeroes(trails))
