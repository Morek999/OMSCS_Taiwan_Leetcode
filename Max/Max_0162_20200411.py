""" 
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


ans = [     
    [1,2,3,1],          # 2
    [1,2,1,3,5,6,4]     # 1 or 5
]
for trails in ans:
    print(Solution().findPeakElement(trails))
