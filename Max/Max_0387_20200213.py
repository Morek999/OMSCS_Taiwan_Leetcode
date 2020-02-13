""" 
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hodling = {}
        for i in s:
            if i not in hodling:
                hodling[i] = 0
            hodling[i] += 1
        for n, i in enumerate(s):
            if hodling[i] == 1:
                return n
        return -1

ans = [
    "leetcode",         # 0
    "loveleetcode",     # 2
    "",
    "cc"
]
for trails in ans:
    print(Solution().firstUniqChar(trails))
