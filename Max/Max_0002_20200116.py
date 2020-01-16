""" 
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode((l1.val + l2.val) % 10)
        tmp = int((l1.val + l2.val) / 10)
        if tmp > 0:
            if l1.next is None:
                l1.next = ListNode(tmp)
            else:
                l1.next.val += tmp
        if l1.next is None:
            if l2.next is None:
                return res
            else:
                l1.next = ListNode(0)
        else:
            if l2.next is None:
                l2.next = ListNode(0)
        res.next = Solution().addTwoNumbers(l1.next, l2.next)
        return res
