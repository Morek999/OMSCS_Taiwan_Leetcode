'''

Idea: My thought is very straightforward. Use an array(dp) to record the maximum value we can get at index i.
Since we can't use the adjacent array value, then the maximum value we can get at i is either the maximum value we can get at i-1, or 
the maximum value we can get from i-2 plus the current value itself. Transfer it to the code is:

dp[i] = max(dp[i-1], dp[i-2] + nums[i])

The initial conditions are i = 0 and 1. When i = 0, the maximum value we can get is definitely nums[0]. When i = 1, the maximum value 
we can get is either nums[0] or nums[1]. From i = 2 we can use a for loop and use the above equation to iterate and get the whole dp 
array. In the end we just need to output dp[n-1], where n is the length of the nums.

Time complexity: O(n) since we need to iterate through the whole nums array   
Space complexity: O(n) since we created an array to store the maximum values that we can get for each position in nums array
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: ## corner case check
            return 0
        
        if len(nums) == 1: ## corner case check
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) ## set up initial condition
        for i in range(2,len(nums)):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1]) ## build the dp array
            
        return max(dp)