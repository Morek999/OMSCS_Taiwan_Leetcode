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
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2) * 1.0
        else:
            return (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a: return b[k]
        if not b: return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]

        if ia + ib < k:
            if ma > mb:
                return self.kth(a, b[ib+1:], k - ib - 1)
            else:
                return self.kth(a[ia+1:], b, k - ia - 1)
        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

        """ 
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        i_min, i_max, half = 0, m, (m + n + 1) // 2
        while i_max >= i_min:
            i = (i_max + i_min) // 2
            j = half - i
            print(f'i={i}  j={j}  half={half}')
            if (i < m) and (nums1[i] < nums2[j-1]):     # i is too small
                i_min = i + 1
            elif (i > 0) and (nums1[i-1] > nums2[j]):   # i is too big
                i_max = i - 1
            else:       # get perfect i
                if i == 0: left_max = nums2[j-1]
                elif j == 0: left_max = nums1[i-1]
                else: left_max = max(nums1[i-1], nums2[j-1])
                
                if (m + n) % 2 == 1:
                    return left_max * 1.0
                
                if i == 0: right_min = nums2[j]
                elif j == 0: right_min = nums1[i]
                else: right_min = min(nums1[i], nums2[j])

                return (left_max + right_min) / 2.0
         """

ans = [
    {'nums1':[1, 3], 'nums2':[2]},    # output: "2.0"
    {'nums1':[1, 2], 'nums2':[3, 4]}  # output: "2.5"
]
for trails in ans:
    print(Solution().findMedianSortedArrays(**trails))
