""" 
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range((len(p) - 1), -1, -1):
                match = (i < len(s)) and (p[j] in {s[i], '.'})
                if ((j+1) < len(p)) and (p[j+1] == '*'):
                    dp[i][j] = dp[i][j+2] or match and dp[i+1][j]
                else:
                    dp[i][j] = match and dp[i+1][j+1]
        return dp[0][0]
        

ans = [
    {'s':'aa', 'p':'a'},        # output: False
    {'s':'aa', 'p':'a*'},       # output: True
    {'s':'ab', 'p':'.*'},       # output: True
    {'s':'aab', 'p':'c*a*b'},       # output: True
    {'s':'mississippi', 'p':'mis*is*p*.'},       # output: False
]
for trails in ans:
    print(Solution().isMatch(**trails))
