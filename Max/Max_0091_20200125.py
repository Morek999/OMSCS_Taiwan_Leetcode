""" 
91. Decode Ways
https://leetcode.com/problems/decode-ways/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        prev_ways = 0
        curr_ways = int(s) > 0
        prev_digi = ''
        for curr_digi in s:
            tmp = curr_ways
            curr_ways = (int(curr_digi) > 0) * curr_ways + (9 < int(prev_digi + curr_digi) < 27) * prev_ways
            prev_ways = tmp
            prev_digi = curr_digi
        return curr_ways
    
ans = [
    '12',   # output = 2
    '226'   # output = 3
]

for trails in ans:
    print(Solution().numDecodings(trails))
