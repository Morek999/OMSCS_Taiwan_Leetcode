# NewConcept
# I take the following pages to form the answer
# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
# Max's script


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[0] = (nums[0])
        maximum = dp[0]
        
        for i in range(1, len(nums)):
            if dp[i-1] > 0:  # if the previous part increase the sum, accepted
                preSum = dp[i-1]
            else: # if previous part decrease the sum, make it zero to skip
                preSum = 0 
            dp[i] = nums[i] + preSum
            maximum = max(maximum, dp[i])

        return maximum
        
