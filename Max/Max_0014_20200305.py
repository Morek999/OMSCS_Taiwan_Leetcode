""" 
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        strs_zip, res = zip(*strs), ""
        for c in strs_zip:
            if len(set(c)) > 1: break
            res += c[0]
        return res

ans = [
    ["flower","flow","flight"],      # output: "fl"
    ["dog","racecar","car"]       # output: ""
]
for trails in ans:
    print(Solution().longestCommonPrefix(trails))
