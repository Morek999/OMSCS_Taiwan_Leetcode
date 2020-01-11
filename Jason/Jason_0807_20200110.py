'''
Idea: Brutal force. Check the maximum number for the each row and column. Then iterate through the grids and for every single grid the value should be 
the smaller value between the row and col maximum value. Calculate the increase and sum up for the entire grids.

Time complexity: O(n^2) since we need to iterate through the entire 2D array
Space complexity: O(n) since we need to create two vectors to record the row and col maximum values

'''
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowlimit = [0]*n
        collimit = [0]*n
        
        for i in range(n):
            rowlimit[i] = max(grid[i])
            for j in range(n):
                collimit[i] = max(collimit[i],grid[j][i])
                
        ans = 0
        
        for row in range(n):
            for col in range(n):
                ans += min(rowlimit[row],collimit[col]) - grid[row][col]
        
        return ans