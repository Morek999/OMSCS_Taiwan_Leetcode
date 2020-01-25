""" 
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])      # m rows, n cols
        r, c = m - 1, 0
        while c < n and r >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
        
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
ans = [
    5,      # output = True
    20      # output = False
]

for trails in ans:
    print(Solution().searchMatrix(matrix=matrix, target=trails))
