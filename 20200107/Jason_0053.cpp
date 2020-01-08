
/*
The explanation I already put in Python part. The reason why I write C++ is just simply because I am not familiar with Python and I use C++ to solve first.
Then I go back and use Python to implement the same thought again.
*/
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        vector<int> dp(nums.size(),0);
        dp[0] = nums[0];
        for(int i = 1; i < nums.size(); i++){
            dp[i] = max(nums[i], nums[i] + dp[i-1]); 
        }
        return *max_element(dp.begin(),dp.end());
    }
};