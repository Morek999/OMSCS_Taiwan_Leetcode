""" 
54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        ans = []
        move = [(0,1), (1,0), (0,-1), (-1,0)]   # move: right (col+1), down (row+1), left (col-1), up (row-1)
        r = c = i = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            matrix[r][c] = False
            nextr, nextc = r + move[i][0], c + move[i][1]
            if (0 <= nextr < R) and (0 <= nextc < C) and (matrix[nextr][nextc] is not False):
                r, c = nextr, nextc
            else:
                i = (i + 1) % 4
                r, c = r + move[i][0], c + move[i][1]
        return ans
    
ans = [
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
]

for trails in ans:
    print(Solution().spiralOrder(trails))
