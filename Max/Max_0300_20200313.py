""" 
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
Time complexity: O()
Space complexity: O()
https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

 """

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        for x in nums:
            # print(f'>> {x}')
            i, j = 0, res
            while i != j:
                # print(f'    i={i}, j={j}')
                m = (i + j) // 2
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            res = max(res, i + 1)
            # print(f'    res={res}, dp={dp}')
        return res

ans = [
    [10,9,2,5,3,7,101,18]       # output: 4
]
for trails in ans:
    print(Solution().lengthOfLIS(trails))
