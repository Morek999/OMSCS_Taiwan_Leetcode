/*
First thought I just came up the brutal force method, by keep another temporary board, you can iterate through the temporary board
then modify the original board. The better way to do this method is just use the first cell of every row and column as a flag. 
This flag would determine whether a row or column has been set to zero. One thing to be careful is that since first cell for both 
first row and first column is the same i.e. matrix[0][0], we can use an additional variable for either the first row/column.

Time complexity: O(MN)
Space complexity: O(1)
*/

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        bool is_col = false;
        
        for(int row = 0; row < m; row++){
            if(matrix[row][0] == 0){
                is_col = true;
            }
            for(int col = 1; col < n; col++){
                if(matrix[row][col]  == 0){
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }
        for(int row = 1; row < m; row++){
            for(int col = 1; col < n; col++){
                if(matrix[row][0] == 0 || matrix[0][col] == 0){
                    matrix[row][col] = 0;
                }
            }
        }
        
        if(matrix[0][0] == 0){
            for(int col = 0; col < n; col++){
                matrix[0][col] = 0;
            }
        }
        
        if(is_col){
            for(int row = 0; row < m; row++){
                matrix[row][0] = 0;
            }
        }
        
    }
};

// Brutal force method
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> temp(m, vector<int> (n,0));
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                temp[row][col] = matrix[row][col];
            }
        }
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if(temp[row][col] == 0){
                    for(int i = 0; i < m; i++){
                        matrix[i][col] = 0;
                    }
                    for(int j = 0; j < n; j++){
                        matrix[row][j] = 0;
                    }
                }
            }
        }
        
    }
};