""" 
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '1': [''],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def backtrack(comb, next_digi):
            if len(next_digi) == 0:
                res.append(comb)
            else:
                for i in phone[next_digi[0]]:
                    backtrack(comb + i, next_digi[1:])
    
        res = []
        if digits:
            backtrack("", digits)
        return res
    
ans = [
    "23"
]

for trails in ans:
    print(Solution().letterCombinations(trails))
