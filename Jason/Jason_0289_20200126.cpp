
// First solution I came out is just use a copy board to simulate the next state and eventually just past the copy board to the original board
// Time Complexity is O(mn) since we need to visit  and space complexity is O(mn) since we need m*n grid
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        vector<vector<int>> copy(m, vector<int>(n,0));
        
        for(int row = 0; row < m; row++){
            for (int col = 0; col < n; col++){
                int lives = 0;
                // scan the 3*3 grid
                for(int rown = max(0, row -1); rown < min(m, row +2); rown++){
                    for(int coln = max(0, col - 1); coln < min(n,col +2); coln++){
                        if(board[rown][coln] == 1){
                            lives++;
                        }
                    }
                }
                if(lives == 3 || lives - board[row][col] == 3){
                    copy[row][col] = 1;
                }
            }
        }
        // shift the bit
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                board[row][col] = copy[row][col];           
            }
        }
    }
};

// bit manipulation method, use the second digit to store the next state, and then just right shift
// Time Complexity is O(mn) since we need to visit  and space complexity is O(1) since we did it in place 
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        int n = board[0].size();
        
        for(int row = 0; row < m; row++){
            for (int col = 0; col < n; col++){
                int lives = 0;
                // scan the 3*3 grid
                for(int rown = max(0, row -1); rown < min(m, row +2); rown++){
                    for(int coln = max(0, col - 1); coln < min(n,col +2); coln++){
                        lives += board[rown][coln] & 1;
                    }
                }
                if(lives == 3 || lives - board[row][col] == 3){
                    board[row][col] |= 0b10;
                }
            }
        }
        // shift the bit
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                board[row][col] >>= 1;
            }
        }
    }
};