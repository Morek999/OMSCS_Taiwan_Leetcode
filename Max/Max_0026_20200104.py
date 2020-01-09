# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[res] = nums[i]
                res += 1
        return res

ans = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4]

]
for trails in ans:
    print(Solution().removeDuplicates(trails))
