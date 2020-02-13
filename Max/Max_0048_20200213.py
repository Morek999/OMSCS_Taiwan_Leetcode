""" 
48. Rotate Image
https://leetcode.com/problems/rotate-image/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for i in range(n):
            matrix[i].reverse()
        print(matrix)

ans = [
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
]
for trails in ans:
    print(Solution().rotate(trails))
