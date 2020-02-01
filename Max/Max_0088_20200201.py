""" 
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        nums1[:] = []
        p1 = p2 = 0
        while (p1 < m) and (p2 < n):
            if tmp[p1] < nums2[p2]:
                nums1.append(tmp[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1 + p2:] = tmp[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

ans = [
    {'nums1':[1,2,3,0,0,0], 'm':3, 'nums2':[2,5,6], 'n':3}     # output = [1,2,2,3,5,6]
]

for trails in ans:
    print(Solution().merge(**trails))
