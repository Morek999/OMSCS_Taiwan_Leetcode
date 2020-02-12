""" 
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topK = []
        counter = {}
        for i in nums:
            if i not in counter: 
                counter[i] = 0
            counter[i] += 1
        for _ in range(k):
            k = max(counter.items(), key=lambda x: x[1])[0]
            topK.append(k)
            counter.pop(k)
        return topK


ans = [
    {'nums':[1,1,1,2,2,3], 'k':2},      # output = [1,2]
    {'nums':[1], 'k':1}                 # output = [1]
]
for trails in ans:
    print(Solution().topKFrequent(**trails))
