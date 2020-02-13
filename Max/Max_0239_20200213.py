""" 
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k * n == 0: return []
        if k == 1: return nums
        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n-1] = nums[n-1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output
            

ans = [
    {'nums':[1,3,-1,-3,5,3,6,7], 'k':3},
    {'nums':[], 'k':0}
]
for trails in ans:
    print(Solution().maxSlidingWindow(**trails))
