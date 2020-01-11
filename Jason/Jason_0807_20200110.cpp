class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rowlimit(n,0);
        vector<int> collimit(n,0);
        for(int i = 0; i < n; i++){
            rowlimit[i] = *max_element(grid[i].begin(),grid[i].end());
            for(int j = 0; j < n; j++){
                collimit[i] = max(collimit[i],grid[j][i]);  
            }
            
        }
        int ans = 0;
        for(int row = 0; row < grid.size(); row++){
            for(int col = 0; col < grid[0].size(); col++){
                ans += min(rowlimit[row],collimit[col]) - grid[row][col];
            }
        }
        return ans;