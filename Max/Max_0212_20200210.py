""" 
212. Word Search II
https://leetcode.com/problems/word-search-ii/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        key = '$'
        trie = {}
        for w in words:
            node = trie
            for l in w:
                node = node.setdefault(l, {})
            node[key] = w

        nrow = len(board)
        ncol = len(board[0])
        match = []
        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            word_match = currNode.pop(key, False)
            if word_match:
                match.append(word_match)
            board[row][col] = '#'

            for (hori, vert) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + hori, col + vert
                if not(0 <= newRow < nrow) or not(0 <= newCol < ncol):
                    continue
                if not(board[newRow][newCol] in currNode):
                    continue
                backtracking(newRow, newCol, currNode)
            board[row][col] = letter

            if not currNode:
                parent.pop(letter)
        
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] in trie:
                    backtracking(r, c, trie)
        return match


ans = [
    {
        'board': [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
            ],
        'words': ["oath","pea","eat","rain"]
    }
]
for trails in ans:
    print(Solution().findWords(**trails))
