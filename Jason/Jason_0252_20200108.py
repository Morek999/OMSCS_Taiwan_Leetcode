
'''
The first idea I came up is to use O(n^2) by checking every single possible combination and see if they are covered with each other.
The function I wrote is by comparing the maximum value of the beginning of the two intervals and minimum value of the ending of the two intervals
I used the method that I previous used in Leetcode 836
https://leetcode.com/problems/rectangle-overlap/solution/
Time complexity is O(n^2) since we need to use double for loop to check 
Space complexity is O(1) since we need two variables to check if there's overlap between two intervals

C++ passed but Python failed at last case QQ
I know there's better solution but I will come back later tomorrow
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def cover(a:List[int],b:List[int]) -> bool:
            minvalue = max(a[0],b[0])
            maxvalue = min(a[1],b[1])
            return minvalue < maxvalue
        
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if cover(intervals[i],intervals[j]):
                    return False
        return True
        