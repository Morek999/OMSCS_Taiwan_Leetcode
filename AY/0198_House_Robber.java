// classic DP
class Solution {
    public int rob(int[] nums) {
        
        int curr = 0;
        int prev = 0;
        for(int i = 0; i < nums.length; i ++) {
            int temp = curr;
            curr = Math.max(prev + nums[i], curr);
            prev = temp;
        }
        
        return curr;
    }
}

// Time: O(n)
// Space: O(1)
