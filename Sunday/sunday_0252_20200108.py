

# 252. Meeting Rooms
# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
#
# Example 1:
# Input: [[0,30], [5,10], [15,20]]
# Output: false

# Example 2:
# Input: [[7,10], [2,4]]
# Output: true

class Solution():
    def meetRoom(self, nums):
        """
        Thought: 
        1. Sort by the start time
        2. For every two consecutive elements
        3. Check the later's start is larger than the former's end
        4. If it doesn't, return False
        Time complexity: O(nlogn)
        Space complexity: O(1).
        """
        
        nums.sort(key=lambda a: a[0])
        for i in range(len(nums)-1):
            if nums[i][-1] > nums[i+1][0]:
                return False
        return True

if __name__ == '__main__':
    cases = [[[0,30], [5,10], [15,20]], [[7,10], [2,4]]] 
    for case in cases:
        print(Solution().meetRoom(case))
