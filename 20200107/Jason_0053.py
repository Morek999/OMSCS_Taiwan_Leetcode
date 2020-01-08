
'''
Idea: The idea is to iterate through the array and use a 1D vector(I called dp) or array to record the maximum sum at every index. 
For example, if we visit component at index i and we want to know if we can add the component at index i to the current subarry, 
then we just need to compare the current value at index i itself and current value at index i add the maximum sum up to index i-1. 
If current value is larger than itself add previous maximum sum, then the subarray should start from i and previous part should be abandoned. 
(dp[i] = max(nums[i], nums[i] + dp[i-1]). After using the for loop to iterate the array, the maximum value in the dp will be the answer. 
Read the code will understand the idea better.

Time Complexity: O(n) since we need to iterate through the nums array
Space Complexity: O(n) since I used an array or vector to record the maximum sum at every index

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 0): ## check corner case
            return 0
        dp = [nums[0]] ## use an array to record the maximum sum at index i. Initially at index 0 there’s no previous component so it will be nums[0]
        for i in range(1,len(nums)):
            dp.append(max(nums[i],dp[i-1] + nums[i])) 
            '''
            at every index i, compare the component at index i and add previous maximum sum, if component itself is larger, 
            then the previous part is useless. Just use the component value and the subarray should start from component at index i
            '''
        return max(dp)
