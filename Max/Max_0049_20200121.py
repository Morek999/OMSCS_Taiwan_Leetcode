""" 
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None: return None
        holding = {}
        for i in strs:
            tmp = tuple(sorted(i))
            if tmp not in holding:
                holding[tmp] = []
            holding[tmp].append(i)
        return holding.values()
        

ans = [
    ["eat", "tea", "tan", "ate", "nat", "bat"]
]

output = [
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
for trails in ans:
    print(Solution().groupAnagrams(trails))
