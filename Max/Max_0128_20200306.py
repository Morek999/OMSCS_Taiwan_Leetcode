""" 
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        tmp, result = set(nums), 0
        if len(tmp) == 1: return 1
        for i in tmp:
            if i - 1 not in tmp:
                curr = i
                streak = 1
                while curr + 1 in tmp:
                    curr += 1
                    streak += 1
                result = max(result, streak)
        return result


ans = [
    [100, 4, 200, 1, 3, 2],      # output: 4
    [0, -1],                     # output: 2
    [1,2,0,1],                   # output: 3
    [0,0]
]
for trails in ans:
    print(Solution().longestConsecutive(trails))
