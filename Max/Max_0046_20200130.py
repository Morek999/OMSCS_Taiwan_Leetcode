""" 
46. Permutations
https://leetcode.com/problems/permutations/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.add_per(nums, [], [])
        
    def add_per(self, l1, l2, res):
        if not l1:
            res.append(l2)
        for i in range(len(l1)):
            self.add_per(l1[:i] + l1[(i+1):], l2 + [l1[i]], res)
        return res
    
ans = [
    [1,2,3]
]

for trails in ans:
    print(Solution().permute(trails))
