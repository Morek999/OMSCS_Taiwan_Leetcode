/*
First I come up with two pass algorithm. First I just count the numbers of 0, 1 and 2s. Then use second round to establish the answer, easy.
Then I check the solution for one pass, and this problem is known as Dutch National Flag Problem and first was proposed by Edsger W. Dijkstra. 
The idea is to attribute a color to each number and then to arrange them following the order of colors on the Dutch flag.
Use three pointers can solve this problem efficiently.
Set p0 as the rightmost boundary of 0, i.e num[idx < p0] = 0 , then set p2 as the leftmost boundary of 2, i.e num[idx > p2] = 2
Then set curr as the index of the current element. Use the while loop to traverse the vector.
While curr <= p2 :

   1. If nums[curr] = 0 : swap currth and p0th elements and move both pointers to the right.

   2. If nums[curr] = 2 : swap currth and p2th elements. Move pointer p2 to the left.

   3. If nums[curr] = 1 : move pointer curr to the right.
 */

// One pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int p0 = 0, curr = 0;
        int p2 = nums.size() - 1;
        
        while(curr <= p2){
            if(nums[curr] == 0){
                swap(nums[curr],nums[p0]);
                curr++;
                p0++;
            }
            else if(nums[curr] == 2){
                swap(nums[curr],nums[p2]);
                p2--;
            }
            else{
                curr++;
            }
        }
    }
};

// Two pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> count(3,0);
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                count[0]++;
            }
            else if(nums[i] == 1){
                count[1]++;
            }
            else{
                count[2]++;
            }
        }
        for(int i = 0; i < nums.size(); i++){
            if(count[0] > 0){
                nums[i] = 0;
                count[0]--;
            }
            else if(count[1] > 0){
                nums[i] = 1;
                count[1]--;
            }
            else{
                nums[i] = 2;
                count[2]--;
            }
        }
        return;
    }
};
