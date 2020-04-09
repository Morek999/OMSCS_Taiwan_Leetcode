""" 
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = finder = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder


ans = [     
    [1,3,4,2,2],
    [3,1,3,4,2]
]
for trails in ans:
    print(Solution().findDuplicate(trails))
