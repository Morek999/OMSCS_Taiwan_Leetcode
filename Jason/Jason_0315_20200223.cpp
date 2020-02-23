/*
Initial thought: brutal force, just check every pair (i,j) and see if nums[j] < nums[i], O(n^2), TLE
So to increase the efficiency, binary search is utilized to insert the nums from the end of the input vectorin a sorted number sequence, 
and the index that the number inserted
will be the number of the elements that are less than nums[i]

Example: [5,2,6,1]  inversed --> [1,6,2,5]

1 ans = 0
1 6 ans = 1
1 2 6 ans = 1
1 2 5 6 ans = 2

Time complexity: O(nlogn) since binary search takes O(log n)
Space complexity: O(n)

Other suggested method: Binary indexed tree (BIT), Binary Search Tree(BST)
reference: https://www.cnblogs.com/grandyang/p/5078490.html
           https://www.youtube.com/watch?v=2SVLYsq5W8M
*/

// Binary search solution

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> sortednum, ans(nums.size());
        for(int i = nums.size()-1; i >= 0; --i){
            int l = 0, r = sortednum.size();
            while(l<r){
                int mid = l + (r-l)/2;
                if(sortednum[mid] >= nums[i]){
                    r = mid;
                }
                else{
                    l = mid + 1;
                }
            }
            ans[i] = r;
            sortednum.insert(sortednum.begin() + r, nums[i]);
            /*or(int j = 0; j < sortednum.size();j++){
                cout << sortednum[j] << " ";
            }
            cout << "ans = " << r << endl;
            */
        }
        return ans;
    }
};

// O(n^2) solution, passes all of the cases but TLE
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        if(nums.empty()){
            return {};
        }
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++){
            int temp = 0;
            for(int j = i+1; j < nums.size(); j++){
                if(nums[j] < nums[i]){
                    temp++;
                }
            }
            ans.push_back(temp);
        }
        return ans;
    }
};