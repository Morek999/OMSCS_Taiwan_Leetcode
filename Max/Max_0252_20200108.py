""" 
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/
Time complexity: O(nlogn) for sorting; then O(n) for checking
Space complexity: O(1)
Solution: First sort the given array and then check whether the ending time of the
    interval is larger than the starting time of the next interval.
 """

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals) <= 1:
            return True
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


ans = [
    [[0,30],[5,10],[15,20]],
    [[7,10],[2,4]]
]
for trails in ans:
    print(Solution().canAttendMeetings(trails))
