""" 
139. Word Break
https://leetcode.com/problems/word-break/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if (w == s[(i-len(w)+1):(i+1)]) and (res[i-len(w)] or i-len(w) == -1):
                    res[i] = True
        return res[-1]
    
ans = [
    {'s':"leetcode", 'wordDict':["leet", "code"]},                      # True
    {'s':"applepenapple", 'wordDict':["apple", "pen"]},                 # True
    {'s':"catsandog", 'wordDict':["cats", "dog", "sand", "and", "cat"]} # False
]

for trails in ans:
    print(Solution().wordBreak(**trails))
