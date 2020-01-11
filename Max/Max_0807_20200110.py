""" 
807. Max Increase to Keep City Skyline
https://leetcode.com/problems/max-increase-to-keep-city-skyline/
Time complexity: O(n^2)
Space complexity: O(n)
Solution: This could use numpy.max(ARRAY, axis=N) to extract skylines. But the 
    run-time will increase a lot in these simple case. Here I use zip(*ARRAY)
    to extract row max. After knowing the skylines, just simply run through 
    the whole grid to find how many levels available to the specific site and 
    sum them up while iterating the grid.
 """

from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sky_row = [max(i) for i in zip(*grid)]
        sky_col = [max(j) for j in grid]
        acc_volume = 0
        for i in range(len(sky_row)):
            for j in range(len(sky_col)):
                acc_volume += min(sky_col[j], sky_row[i]) - grid[i][j]
        return acc_volume

ans = [
    [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
]
for trails in ans:
    print(Solution().maxIncreaseKeepingSkyline(trails))
