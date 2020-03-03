""" 
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            res = [nums.index(target)]
        except ValueError:
            return [-1, -1]
        res.append(len(nums) - 1 - sorted(nums, reverse=True).index(target))
        return res

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind_left = self.bin_search(nums, target, True)
        if ind_left == len(nums) or nums[ind_left] != target:
            return [-1, -1]
        return [ind_left, self.bin_search(nums, target, False)]
    
    def bin_search(self, nums, target, left):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if (nums[mid] > target) or (left and (target == nums[mid])):
                r = mid
            else:
                l = mid + 1
        return l

ans = [
    {'nums': [5,7,7,8,8,10], 'target': 8},      # output: [3,4]
    {'nums': [5,7,7,8,8,10], 'target': 6}       # output: [-1,-1]
]
for trails in ans:
    print(Solution().searchRange(**trails))
