/* 
    The key idea of this problem is that the volume of the water can be trapped in index i 
    vol = min(max(h[0:i-1]), max(h[i:end]) - h[i]
    so if we do brutal force, loop through the vector and then search maximum element on left and right side, it's O(n^2) time complexity
    and fortunately it will pass. Space complexity is O(1) since we only need two variables to keep updating the left and right maximum value
*/


class Solution {
public:
    int trap(vector<int>& height) {
        
        if(height.empty()){
            return 0;
        }
        int n = height.size();
        int ans = 0;

        for(int i = 0; i < n; i++){
            int l = *max_element(height.begin(),height.begin()+i+1);
            int r = *max_element(height.begin()+i, height.end());
            ans += min(l,r) - height[i];
        }
        return ans;
    }
};


class Solution {
public:
    int trap(vector<int>& height) {
        /* 
        Since in the brutal force method, actually the maximum element on the left and right side can be pre-computed. This fact leads to the second solution
        using DP. Define the two vectors l and r, where l[i] = max(h[0:i-1]) and r[i] = max(h[i:n-1]), n is the height array size
        We just need to use two for loops to find the l and r vector (be careful about the boundary) 
        
        l[i] = max(h[i],l[i-1]), i = 0 ~ n-1
        h[i] = max(h[i], r[i+1]), where i = n-1 ~ 0
        
        The we can just use one for loop to find the ans, ans += min(l[i],r[i]) - h[i]
        Time complexity: O(n) since we have used for loop three times
        Space complexity: O(n) since we need two vectors to store l and r 
        */
        if(height.empty()){
            return 0;
        }
        int n = height.size();
        int ans = 0;
        vector<int> l(n);
        vector<int> r(n);
        
        //find the l vector
        for(int i = 0; i < n; i++){
            if(i == 0){
                l[i] = height[i];
            }
            else{
                l[i] = max(l[i-1],height[i]);
            }
        }
        // find the r vector
        for(int i = n-1; i >= 0; i--){
            if(i == n-1){
                r[i] = height[i];
            }
            else{
                r[i] = max(r[i+1],height[i]);
            }
        }
        
        // calculate the answer
        for(int i = 0; i < n; i++){
            ans += min(l[i],r[i]) - height[i];
        }
        return ans;
    }
};

class Solution {
public:
    int trap(vector<int>& height) {
        /*
        This method is the optimal solution, which further reduce the space complexity, but it's not that straight forward.
        We can use two variables to track the max_l and max_r and use two pointers to go from left and right.
        Since actually the volume to be stored at every index i is determined by the smaller value of the two side max, we 
        only need to update one variable at every single step.

        the pseudo code is like this:
        while l < r:
           if max_l < max_r:
              ans += max_l - h[l]
              l++ --> move
              max_l = max(max_l,h[l]) --> update
              
           else:
              ans += max_r - h[l]
              r-- --> move
              max_r = max(max_r,h[r]) --> update
              

        if two side meet(l == r) then we finish the calculation
        Reference: https://www.youtube.com/watch?v=StH5vntauyQ
        */
        if(height.empty()){
            return 0;
        }
        int l = 0, r = height.size() - 1;
        int max_l = height[l];
        int max_r = height[r];
        int ans = 0;
        
        while(l < r){
            if (max_l < max_r){
                ans += max_l - height[l];
                l++;
                max_l = max(max_l, height[l]);
                
            }
            else{
                ans += max_r - height[r];
                r--;
                max_r = max(max_r,height[r]);
            }
        }
        return ans;
    }
};