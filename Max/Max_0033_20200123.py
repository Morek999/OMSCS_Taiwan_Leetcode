""" 
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

        """ 
        if target in nums:
            return nums.index(target)
        return -1
         """
         
ans = [
    {'nums':[4,5,6,7,0,1,2], 'target':0},
    {'nums':[4,5,6,7,0,1,2], 'target':3}
]

for trails in ans:
    print(Solution().search(**trails))
