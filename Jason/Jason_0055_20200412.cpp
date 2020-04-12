/*
The method I came up is very simple, just use a variable called maxreach to record the maximum index that could be reached.
Then just traverse the loop, for every single index, and if the index is reachable(i.e maxreach >= index), the maximum reach for this index 
will be its index + its value. Then just keep updating the maxreach. In the end just compare the maxreach and the nums size

Time complexity: O(n) since we need to iterate through the entire vector
Space complexity: O(1) since we only need one variable to record the maxreach
*/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxreach = 0;
        for(int i = 0; i < nums.size(); i++){
            int temp = 0;
            if(maxreach >= i){
                temp = i + nums[i];
            }
            maxreach = max(maxreach,temp);
        }
        return maxreach >= nums.size()-1;
    }
};