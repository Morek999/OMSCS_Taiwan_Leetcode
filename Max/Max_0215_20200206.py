""" 
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
        

ans = [
    {'nums':[3,2,1,5,6,4], 'k':2},          # output: 5
    {'nums':[3,2,3,1,2,4,5,5,6], 'k':4}     # output: 4
]
for trails in ans:
    print(Solution().findKthLargest(**trails))
