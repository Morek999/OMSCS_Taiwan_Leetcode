""" 
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
Time complexity: O()
Space complexity: O()
Solution: 
 """

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while (curr != None) :
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

LN = [
    [1,2,3,4,5]
]
ans = []
for i in range(len(LN)):
    ans.append(ListNode(LN[i][0]))
    tmp = ans[-1]
    for j in range(1, len(LN[i])):
        tmp.next = ListNode(LN[i][j])
        tmp = tmp.next

for trails in ans:
    print(Solution().reverseList(trails))
