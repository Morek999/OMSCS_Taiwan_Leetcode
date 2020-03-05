""" 
344. Reverse String
https://leetcode.com/problems/reverse-string/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

ans = [
    ["h","e","l","l","o"],      # output: ["o","l","l","e","h"]
    ["H","a","n","n","a","h"]       # output: ["h","a","n","n","a","H"]
]
for trails in ans:
    print(Solution().reverseString(trails))
