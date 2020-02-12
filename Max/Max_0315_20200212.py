""" 
315. Count of Smaller Numbers After Self
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        def sort_index(nums_list):
            half = len(nums_list) // 2
            if half:
                left, right = sort_index(nums_list[:half]), sort_index(nums_list[half:])
                for i in range(len(nums_list))[::-1]:
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        res[left[-1]] += len(right)
                        nums_list[i] = left.pop()
                    else:
                        nums_list[i] = right.pop()
            return nums_list
        sort_index(list(range(len(nums))))
        return res


ans = [
    [5,2,6,1]       # [2,1,1,0]
]
for trails in ans:
    print(Solution().countSmaller(trails))
