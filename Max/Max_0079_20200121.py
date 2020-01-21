""" 
79. Word Search
https://leetcode.com/problems/word-search/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = self.backtrack(board,m,n,i,j,word[1:])
                    if res:
                        return True
        return False
        
        
    def backtrack(self, board,m,n, i, j, target):
        temp = board[i][j]
        if len(target) == 0:
            return True
        board[i][j] = '#'
        for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=x<m and 0<=y<n and target[0] == board[x][y]:
                dec = self.backtrack(board,m,n,x,y,target[1:])
                if dec:
                    return True
        board[i][j] = temp
        return False
        
""" 
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.sink(board, x, y, word):
                    return True
        return False
    
    def sink(self, board, x, y, word):
        if len(word) == 0: 
            return True
        if (x < 0) or (x >= len(board)) or (y < 0) or (y >= len(board[0])) or (word[0] != board[x][y]):
            return False
        tmp = board[x][y]
        board[x][y] = '#'
        res = self.sink(board, x-1, y, word[1:]) or self.sink(board, x+1, y, word[1:]) \
            or self.sink(board, x, y-1, word[1:]) or self.sink(board, x, y+1, word[1:])
        board[x][y] = tmp
        return res
 """

ans = [
    "ABCCED",   # true
    "SEE",      # true
    "ABCB"      # false
]

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

for trails in ans:
    print(Solution().exist(board=board, word=trails))
