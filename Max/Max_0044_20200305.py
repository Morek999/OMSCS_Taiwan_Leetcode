""" 
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = p_idx = 0
        star_idx = s_tmp_idx = -1
        while s_idx < len(s):
            if (p_idx < len(p)) and (p[p_idx] in ['?', s[s_idx]]):
                s_idx += 1
                p_idx += 1
            elif (p_idx < len(p)) and (p[p_idx] == '*'):
                star_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1
            elif star_idx == -1:
                return False
            else:
                p_idx = star_idx + 1
                s_tmp_idx = s_idx = s_tmp_idx + 1
        return all(x == '*' for x in p[p_idx:])

ans = [
    {'s': "aa", 'p':'a'},      # output: false
    {'s': "aa", 'p':'*'},      # output: true
    {'s': "cb", 'p':'?a'},      # output: false
    {'s': "adceb", 'p':'a*b'},      # output: true
    {'s': "acdcb", 'p':'a*c?b'}      # output: true
]
for trails in ans:
    print(Solution().isMatch(**trails))
