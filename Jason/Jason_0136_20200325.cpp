/*
First I came out the brutal force method by using a hash set to record the seen number. Use a for loop to traverse the numbers,
if first time see it, just insert to the hash set and add it to the sum. If seen it before, just minus the value, since the other numbers
will appear twice, in the end the sum will be the answer. This is O(n) method, but we need O(n) time complexity since we need n/2 items in
hash set. 
A better way to optimize it is bit operation, using XOR operation:
  1. If we take XOR of zero and some bit, it will return that bit, a XOR 0 = a
  2. If we take XOR of two same bits, it will return 0, a XOR a = 0
  3. By using 1 and 2, a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b

So just XOR all bits, the unique number can be found, fucking amazing!
Time complexity: O(n)
Space complexity: O(1)
 */

// bit operation method
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(int i = 0; i < nums.size(); i++){
            ans ^= nums[i];
        }
        return ans;
    }
};

// brutal force by using hash set
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        unordered_set<int> seen;
        for(int i = 0; i < nums.size(); i++){
            if(seen.find(nums[i]) != seen.end()){
                ans -= nums[i];
            }
            else{
                seen.insert(nums[i]);
                ans += nums[i];
            }
        }
        return ans;
    }
};