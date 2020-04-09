""" 
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        nrow = len(matrix)
        ncol = len(matrix[0])
        for row in range(nrow):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, ncol):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, nrow):
            for col in range(1, ncol):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0
        
        if matrix[0][0] == 0:
            for col in range(ncol):
                matrix[0][col] = 0
        
        if is_col:
            for row in range(nrow):
                matrix[row][0] = 0
        
        print(matrix)


ans = [     
    [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ],
    [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
]
for trails in ans:
    print(Solution().setZeroes(trails))
