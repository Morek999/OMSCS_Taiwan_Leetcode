""" 
179. Largest Number
https://leetcode.com/problems/largest-number/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # if not any(nums): return "0"
        # return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))

        # merge sort
        nums = self.mergesort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))
    
    def mergesort(self, nums, l, r):
        if l > r: return []
        if l == r : return [nums[l]]
        mid = (l + r) // 2
        left = self.mergesort(nums, l, mid)
        right = self.mergesort(nums, mid+1, r)
        return self.merge(left, right)
    
    def merge(self, l, r):
        res, i, j = [], 0, 0
        while (i < len(l)) and (j < len(r)):
            if str(l[i]) + str(r[j]) >= str(r[j]) + str(l[i]):
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        res.extend(l[i:] or r[j:])
        return res


ans = [     
    [10,2],  # 210
    [3,30,34,5,9]
]
for trails in ans:
    print(Solution().largestNumber(trails))
