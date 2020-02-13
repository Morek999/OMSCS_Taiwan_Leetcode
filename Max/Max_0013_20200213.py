""" 
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M':1000
        }
        rule = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M'], 'V':[], 'L':[], 'D':[], 'M':[]}
        res = []
        for i in range(len(s) - 1):
            if s[i+1] in rule[s[i]]:
                res.append(-roman[s[i]])
            else:
                res.append(roman[s[i]])
        res.append(roman[s[len(s) - 1]])
        return sum(res)

ans = [
    "III",
    "IV",
    "IX",
    "LVIII",
    "MCMXCIV"
]
for trails in ans:
    print(Solution().romanToInt(trails))
