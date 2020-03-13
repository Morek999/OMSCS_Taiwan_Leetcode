""" 
78. Subsets
https://leetcode.com/problems/subsets/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [curr + [i] for curr in res]
            # print(res)
        return res

ans = [
    [1,2,3]
]
for trails in ans:
    print(Solution().subsets(trails))
