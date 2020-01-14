""" 
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
Time complexity: O(n)
Space complexity: O(1)
Solution: 
 """

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        water = max_l = max_r = 0
        pt_l = 0
        pt_r = len(height) - 1
        while pt_l < pt_r:
            if height[pt_l] < height[pt_r]:
                if height[pt_l] >= max_l:
                    max_l = height[pt_l]
                else:
                    water += max_l - height[pt_l]
                pt_l += 1
            else:
                if height[pt_r] >= max_r:
                    max_r = height[pt_r]
                else:
                    water += max_r - height[pt_r]
                pt_r -= 1
        return water

ans = [
    [0,1,0,2,1,0,1,3,2,1,2,1]   # output: 6
]
for trails in ans:
    print(Solution().trap(trails))
