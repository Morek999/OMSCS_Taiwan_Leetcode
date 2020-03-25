""" 
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0: return 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        m = len(matrix)
        n = len(matrix[0])
        cache = {i:{j:0 for j in range(n)} for i in range(m)}
        ans = 0
        
        def dfs(matrix, i, j, cache):
            if cache[i][j] != 0:
                return cache[i][j]
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if (0 <= x < m) and (0 <= y < n) and (matrix[x][y] > matrix[i][j]):
                    cache[i][j] = max(cache[i][j], dfs(matrix, x, y, cache))
            cache[i][j] += 1
            return cache[i][j]
        
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(matrix, i, j, cache))
        
        return ans


ans = [     # 4, 4
    [
        [9,9,4],
        [6,6,8],
        [2,1,1]
    ],
    [
        [3,4,5],
        [3,2,6],
        [2,2,1]
    ] 
]
for trails in ans:
    print(Solution().singleNumber(trails))
