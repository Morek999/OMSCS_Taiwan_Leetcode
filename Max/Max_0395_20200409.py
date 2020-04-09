""" 
395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(tmp, k) for tmp in s.split(c))
        return len(s)

ans = [     
    {'s':"aaabb", 'k':3},   # 3
    {'s':"ababbc", 'k':2}   # 5
]
for trails in ans:
    print(Solution().longestSubstring(**trails))
