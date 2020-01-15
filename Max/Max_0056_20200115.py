""" 
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Time complexity: O(nlogn)
Space complexity: O(n)
Solution: 
 """

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        holding = []
        for i in intervals:
            if holding and i[0] <= holding[-1][1]:
                holding[-1][1] = max(holding[-1][1], i[1])
            else:
                holding.append(i)
        return holding

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     if len(intervals) <= 1: return intervals
    #     intervals.sort()
    #     holding = [intervals[0]]
    #     for i in range(1, len(intervals)):
    #         if holding[-1][1] >= intervals[i][0]:
    #             if holding[-1][1] < intervals[i][1]:
    #                 holding[-1][1] = intervals[i][1]
    #         else:
    #             holding.append(intervals[i])
    #     return holding



ans = [
    [[1,3],[2,6],[8,10],[15,18]],    # output: [[1,6],[8,10],[15,18]]
    [[1,4],[4,5]],  # output: [[1,5]]
    [[1,4],[2,3]]   # output: [[1,4]]
]
for trails in ans:
    print(Solution().merge(trails))
