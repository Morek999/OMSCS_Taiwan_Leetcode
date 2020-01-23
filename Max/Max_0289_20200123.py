""" 
289. Game of Life
https://leetcode.com/problems/game-of-life/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Do not return anything, modify board in-place instead.
        neighbor = [(i-1, j-1) for i in range(3) for j in range(3)]
        neighbor.remove((0, 0))
        nrow = len(board)
        ncol = len(board[0])
        tmp = [[-1] * ncol] * nrow
        for x in range(nrow):
            for y in range(ncol):
                live = 0
                for n in neighbor:
                    r = x + n[0]
                    c = y + n[1]
                    if (0 <= r < nrow) and (0 <= c < ncol) and (abs(board[r][c]) == 1):
                        live += 1
                tmp[x][y] = live
                if (board[x][y] == 1) and ((live < 2) or (live > 3)):
                    board[x][y] = -1
                if (board[x][y] == 0) and (live == 3):
                    board[x][y] = 2
        for x in range(nrow):
            for y in range(ncol):
                board[x][y] = 1 if board[x][y] > 0 else 0
        for i in (tmp, board):
            for j in i:
                print(j)
            print('----')
        
ans = [
    [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
]

for trails in ans:
    print(Solution().gameOfLife(trails))
