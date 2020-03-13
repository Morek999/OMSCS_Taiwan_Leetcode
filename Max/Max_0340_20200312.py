""" 
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Time complexity: O()
Space complexity: O()
 """

from typing import List
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or len(s) == 0: return 0
        pt_l = pt_r = 0
        max_len = 1
        hashmap = defaultdict()

        while pt_r < len(s):
            hashmap[s[pt_r]] = pt_r
            pt_r += 1
            if len(hashmap) == k + 1:
                ind = min(hashmap.values())
                hashmap.pop(s[ind])
                pt_l = ind + 1
            max_len = max(max_len, pt_r - pt_l)
        
        return max_len

ans = [
    {'s': "eceba", 'k': 2}, # 3
    {'s': "aa", 'k': 1}     # 2
]
for trails in ans:
    print(Solution().lengthOfLongestSubstringKDistinct(**trails))
