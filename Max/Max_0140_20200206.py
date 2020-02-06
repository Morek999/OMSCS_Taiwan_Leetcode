""" 
140. Word Break II
https://leetcode.com/problems/word-break-ii/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        self.holding = {}
        return self.sentences(s)

    def sentences(self, s):
        if s in self.holding:
            return self.holding[s]
        if not s:
            return []
        res = []
        for w in self.wordDict:
            if not s.startswith(w):
                continue
            if len(w) == len(s):
                res.append(w)
            else:
                remain = self.sentences(s[len(w):])
                for i in remain:
                    res.append(w + ' ' + i)
        self.holding[s] = res
        return res

ans = [
    {'s': "catsanddog", 'wordDict': ["cat", "cats", "and", "sand", "dog"]},
    {'s': "pineapplepenapple", 'wordDict': ["apple", "pen", "applepen", "pine", "pineapple"]}
]
for trails in ans:
    print(Solution().wordBreak(**trails))
