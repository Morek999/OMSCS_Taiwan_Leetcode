""" 
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [0 for _ in range(i + 1)]
            row[0] = row[-1] = 1
            for j in range(1, len(row)-1):
                row[j] = result[i-1][j-1] + result[i-1][j]
            result.append(row)
        return result


ans = [     
    5
]
for trails in ans:
    print(Solution().generate(trails))
