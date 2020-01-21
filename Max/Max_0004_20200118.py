""" 
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

ans = [
    {'nums1'=[1, 3], 'nums2'=[2]},    # output: "2.0"
    {'nums1'=[1, 2], 'nums2'=[3, 4]}  # output: "2.5"
]
for trails in ans:
    print(Solution().longestPalindrome(**trails))
