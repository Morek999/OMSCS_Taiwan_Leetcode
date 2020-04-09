""" 
55. Jump Game
https://leetcode.com/problems/jump-game/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(last, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


ans = [     
    [2,3,1,1,4],
    [3,2,1,0,4]
]
for trails in ans:
    print(Solution().canJump(trails))
