""" 
62. Unique Paths
https://leetcode.com/problems/unique-paths/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        return d[m-1][n-1]
        

ans = [     
    {'m':3, 'n':2},     # 3
    {'m':7, 'n':3}      # 28
]
for trails in ans:
    print(Solution().generate(trails))
