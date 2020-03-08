/*
Method 1: linear scan , this is my initial thought with O(n) complexity, but since this question requires O(log n) and is sorted problem,
then I came up with the binary search method.

Method 2: binary search, since it's sorted array it's easy to use binary search to find the target, but the tricky part is that
by we need to find the first and the last index, so if nums[mid] == target, we need to decide whether we go right or left by 
introducing the bool variable left. If left is true that means we are looking for the first number == target.
If it's false then we are looking for the first number that is larger than the target, then we - 1 we will get the last number == target.
Time complexity : O(log n)
Space complexity: O(1)
*/
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans(2,-1);
        int l = binarysearch(nums,target, true);
        
        if(l == nums.size() || nums[l] != target){
            return ans;
        }
        ans[0] = l;
        ans[1] = binarysearch(nums,target, false) - 1;
        return ans;
    }
    
    int binarysearch(vector<int>& nums, int target, bool left){
        int l = 0, r = nums.size();
        while(l < r){
            int mid = l + (r - l) / 2;
            if(nums[mid] > target || (left && target == nums[mid])){
                r = mid;
            }
            else{
                l = mid + 1;
            }
        }
        return l;
    }
};





class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans(2,-1);
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == target){
                ans[0] = i;
                break;
            }
        }
        if(ans[0] == -1){
            return ans;
        }
        for(int i = nums.size() - 1; i >= 0; i--){
            if(nums[i] == target){
                ans[1] = i;
                break;
            }
        }
        return ans;
    }
};