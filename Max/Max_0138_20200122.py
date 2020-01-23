""" 
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        

