""" 
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(len(s)):
                if s[:i+1] == s[i::-1]:
                    path.append(s[:i+1])
                    dfs(s[i+1:], path, res)
                    path.pop()
        res = []
        dfs(s, [], res)
        return res


ans = [     
    "aab"
]
for trails in ans:
    print(Solution().partition(trails))
