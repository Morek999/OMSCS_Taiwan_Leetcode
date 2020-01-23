""" 
15. 3Sum
https://leetcode.com/problems/3sum/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums [l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums [l], nums[r]])
                    while (l < r) and (nums[l] == nums[l+1]):
                        l += 1
                    while (l < r) and (nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
        return res

ans = [
    [-1, 0, 1, 2, -1, -4]
]

""" 
[
  [-1, 0, 1],
  [-1, -1, 2]
]
 """

for trails in ans:
    print(Solution().threeSum(trails))
