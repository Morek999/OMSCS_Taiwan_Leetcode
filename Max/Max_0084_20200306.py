""" 
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        area_max = 0
        for i in range(len(heights)):
            while (stack[-1] != -1) and (heights[stack[-1]] >= heights[i]):
                area_max = max(area_max, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while (stack[-1] != -1):
            area_max = max(area_max, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return area_max

ans = [
    [2,1,5,6,2,3]   # output: 10
]
for trails in ans:
    print(Solution().largestRectangleArea(trails))
