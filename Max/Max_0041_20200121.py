""" 
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
Time complexity: O(N)
Space complexity: O(1)
Solution: 
 """

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for i in range(len(nums)+1):
            if i+1 not in nums: return i+1

ans = [
    [1,2,0],        # output: "3"
    [3,4,-1,1],     # output: "2"
    [7,8,9,11,12]   # output: "1"
]
for trails in ans:
    print(Solution().longestPalindrome(**trails))
