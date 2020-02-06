""" 
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        f s == '': return True
        s = ''.join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]

        

ans = [
    "A man, a plan, a canal: Panama",   # output = True
    "race a car",    # output = False
    '0P'
]
for trails in ans:
    print(Solution().isPalindrome(trails))
