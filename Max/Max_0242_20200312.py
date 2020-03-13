""" 
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = +1 if (s[i] not in dic) else (dic[s[i]] + 1)
            dic[t[i]] = -1 if (t[i] not in dic) else (dic[t[i]] - 1)
        for i in dic.values():
            if i != 0: return False
        return True

ans = [
    {'s': "anagram", 't': 'nagaram'}, 
    {'s': "rat", 't': 'car'}
]
for trails in ans:
    print(Solution().isAnagram(**trails))
