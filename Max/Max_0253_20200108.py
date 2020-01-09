""" 
253. Meeting Rooms
https://leetcode.com/problems/meeting-rooms-ii/
Time complexity: O(nlogn) for sorting; then O(n) for checking
Space complexity: O(n)
Solution: This method separates the start time and end time and track with the strat time 
    to see whether any meeting has finished. This will messed up the list but we are only
    required to answer how many meeting rooms should be prepared rather than arranging.
 """

from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 1: return 0
        
        rooms = 0
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        pointer = 0

        for i in range(len(intervals)):
            if starts[i] >= ends[pointer]:
                rooms -= 1
                pointer += 1
            rooms += 1
        return rooms


ans = [
    [[0,30],[5,10],[15,20]],
    [[7,10],[2,4]],
    [(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)]
]
for trails in ans:
    print(Solution().minMeetingRooms(trails))
