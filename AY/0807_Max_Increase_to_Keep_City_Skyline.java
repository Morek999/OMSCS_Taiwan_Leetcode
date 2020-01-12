class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
        int len_i = grid.length;
        int len_j = grid[0].length;
        
        int[] skyline_TB = new int[len_j];
        int[] skyline_LR = new int[len_i];
        
        for (int i = 0; i < len_i; i ++ ) {
            for (int j = 0; j < len_j; j ++) {
                if (grid[i][j] > skyline_TB[i]) skyline_TB[i] = grid[i][j];
                if (grid[i][j] > skyline_LR[j]) skyline_LR[j] = grid[i][j];
            }
        }
        int newBuild = 0;
        for (int i = 0; i < len_i; i ++ ) {
            for (int j = 0; j < len_j; j ++) {
                int canReach = Math.min(skyline_TB[i], skyline_LR[j]);
                if (grid[i][j] != canReach) newBuild += canReach - grid[i][j] ;
            }
        }
        return newBuild;
        
    }
}


// Time: O(n^2)
// Space: O(n)
