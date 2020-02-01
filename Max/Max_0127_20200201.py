""" 
127. Word Ladder
https://leetcode.com/problems/word-ladder/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (not beginWord) or (not endWord) or (not wordList):
            return 0
        L = len(beginWord)
        all_combo_dict = collections.defaultdict(list)
        for w in wordList:
            for i in range(L):
                all_combo_dict[w[:i] + '*' + w[(i+1):]].append(w)
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            curr_w, level = queue.popleft()
            for i in range(L):
                inter_w = curr_w[:i] + '*' + curr_w[(i+1):]
                for w in all_combo_dict[inter_w]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited[w] = True
                        queue.append((w, level+1))
                all_combo_dict[inter_w] = []
        return 0

ans = [
    {'beginWord':"hit",
    'endWord':"cog",
    'wordList':["hot","dot","dog","lot","log","cog"]}     # output = 5
]

for trails in ans:
    print(Solution().ladderLength(**trails))
