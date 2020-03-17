""" 
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = imax = imin = nums[0]
        print(f'>> res={res}, max={imax}, min={imin}')
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])
            res = max(res, imax)
            print(f'    > nums[i]={nums[i]} : res={res}, max={imax}, min={imin}')
        return res

ans = [
    [2,3,-2,4, -1], # 6
    [-2,0,-1]   # 0
]
for trails in ans:
    print(Solution().maxProduct(trails))
