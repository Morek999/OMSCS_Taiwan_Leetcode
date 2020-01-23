""" 
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        if not nums: return None
        pi = pj = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            j = -1 - i      # reversed pointer
            res[i] *= pi
            res[j] *= pj
            pi *= nums[i]
            pj *= nums[j]
        return res
        """
        l = len(nums)
        a = [1] * l
        b = [1] * l
        for i in range(1, l):
            if i > 0: a[i] = a[i-1] * nums[i-1]
            if i < l: b[l-i-1] = b[l-i] * nums[l-i]
        return [a[i] * b[i] for i in range(l)]
         """

ans = [
    [1,2,3,4]
]

for trails in ans:
    print(Solution().productExceptSelf(trails))
