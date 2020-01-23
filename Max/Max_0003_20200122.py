""" 
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        window = ''
        ans = 0
        for i in list(s):
            if i in window:
                ans = len(window) if len(window) > ans else ans
                window = window[(window.find(i) + 1):] + i
            else:
                window += i
        ans = len(window) if len(window) > ans else ans
        return ans

ans = [
    "abcabcbb",   # 3
    "bbbbb",      # 1
    "pwwkew",     # 3
    " ",          # 1
    'aab',        # 2
    'dvdf'        # 3
]

for trails in ans:
    print(Solution().lengthOfLongestSubstring(trails))
