""" 
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = l = 0
        r = len(height) - 1
        while l < r:
            res = max(res, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

ans = [
    [1,8,6,2,5,4,8,3,7]     # output = 49
]

for trails in ans:
    print(Solution().maxArea(trails))
