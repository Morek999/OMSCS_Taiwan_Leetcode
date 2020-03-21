""" 
269. Alien Dictionary
https://leetcode.com/problems/alien-dictionary/
Time complexity: O()
Space complexity: O()
 """

from typing import List
class Solution(object):
    def alienOrder(self, words):
        self.graph = {}
        
        for word in words:
            for c in word:
                self.graph[c] = []
                
        for i in range(1, len(words)):
            j = 0
            if words[i - 1] == words[i]:
                continue
            first_word_len = len(words[i - 1])
            second_word_len = len(words[i])
            
            while j < first_word_len and j < second_word_len and words[i - 1][j] == words[i][j]:
                j += 1
                
            if j == second_word_len:
                return ""
            
            if j != first_word_len:
                self.graph[words[i - 1][j]].append(words[i][j])
                
        total_items = len(self.graph)
        self.res = [""] * total_items
        self.idx = 0
        self.visited = {}
        self.traversed = {} 
        self.isCycle = False
        for key in self.graph.keys():
            self.visited[key] = False
            self.traversed[key] = False
            
        for key in self.graph.keys():
            if not self.visited[key]:
                self.visited[key] = True
                if self.dfs(key):
                    return ""
                
        self.res.reverse()
        return "".join(self.res)
    
    
    def dfs(self, key):
        self.traversed[key] = True
        
        for child in self.graph[key]:
            if self.traversed[child]:
                return True
            if not self.visited[child]:
                self.visited[child] = True
                res = self.dfs(child)
                if res:
                    return True
        
        self.traversed[key] = False
        self.res[self.idx] = key
        self.idx += 1
        return False


ans = [
    [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ],          # "wertf"
    [
        "z",
        "x"
    ]           # "zx"
]
for trails in ans:
    print(Solution().alienOrder(trails))
