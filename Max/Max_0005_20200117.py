""" 
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLP(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        holding = ''
        for i in range(len(s)):
            holding = max(findLP(s, i, i), findLP(s, i, i+1), holding, key=len)
        return holding

ans = [
    "babad",    # output: "bab"
    "cbbd"  # output: "bb"
]
for trails in ans:
    print(Solution().longestPalindrome(trails))
