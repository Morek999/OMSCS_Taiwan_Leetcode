""" 
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(i, j):
            if (0 <= i < len(grid)) and (0 <= j < len(grid[i])) and (grid[i][j] == '1'):
                grid[i][j] = '0'
                list(map(sink, (i-1, i+1, i, i), (j, j, j-1, j+1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
""" 
        island = 0
        for nrow, row in enumerate(grid):
            for ni, i in enumerate(row):
                if i == '1':
                    if ni < len(row) - 1:
                        if grid[nrow][ni + 1] != -1:
                            island += 1
                    else:
                        island += 1
                    grid[nrow][ni] = -1
                if i != '0':
                    if ni < len(row) - 1:       # check the right cell of i
                        grid[nrow][ni + 1] = -1 if grid[nrow][ni + 1] == '1' else grid[nrow][ni + 1]
                    if nrow < len(grid) - 1:    # check the down cell of i
                        grid[nrow + 1][ni] = -1 if grid[nrow + 1][ni] == '1' else grid[nrow + 1][ni]

                    
                # print(f'({nrow},{ni}) -> {grid[nrow][ni]} : {i} : {island}')
                # print(grid)
        return island
 """

ans = [
    [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']],  # output: 1
    [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']],  # output: 3
    [["1","1","1"],["0","1","0"],["1","1","1"]],     # output: 1
    [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]     # output: 1
]

for trails in ans:
    print(Solution().numIslands(trails))
