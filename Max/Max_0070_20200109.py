""" 
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Time complexity: O(n)
Space complexity: O(n)
Solution: This is Fibonacci series. Stairs could be climbed by 1-step from the previous
    stairs (i-1), or 2-step from the 2-step-previous stairs (i-2).
 """

from typing import List
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0: return 0
        if n == 1: return n
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]

ans = [
    2,
    3,
    4
]
for trails in ans:
    print(Solution().climbStairs(trails))
