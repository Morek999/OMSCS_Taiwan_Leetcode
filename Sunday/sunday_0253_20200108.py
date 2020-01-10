# newConcept
# Scanning line

# Take reference from: 
# https://github.com/ChenglongChen/LeetCode-3/blob/master/Python/meeting-rooms-ii.py
# http://52.14.116.56/2018/09/16/LeetCode/0253-Meeting-Rooms-II/
# 

# 253. Meeting Rooms II
# Given an array of meeting time intervals consisting of start and end time
# [[s1,e1], [s2,e2],...] (si < ei), find
# the minimun number of conference rooms required.

# Example 1:
# Input: [[0,30], [5,10], [15,20]]
# Outpt: 2

# Example 2:
# Inpute: [[7,10], [2,4]]
# Output: 1


class Solution():
    def minMeetRooms(self, intervals):
        """
        
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[-1])
        
        starts.sort()
        ends.sort()

        s, e = 0, 0
        minRooms, cntRooms = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                cntRooms += 1  # Acquire a room.
                # Update the min number of rooms.
                minRooms = max(minRooms, cntRooms)
                s += 1
            else:
                cntRooms -= 1  # Release a room.
                e += 1

        return minRooms


if __name__ == '__main__':
    cases = [[[0,30], [5,10], [15,20]], [[7,10], [2,4]]] 
    for case in cases:
        print(Solution().minMeetRooms(case))
