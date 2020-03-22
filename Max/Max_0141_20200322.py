""" 
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
Time complexity: O()
Space complexity: O()
 """

from typing import List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head is None) or (head.next is None):
            return False
        slow = head
        fast = head.next
        while (slow != fast):
            if (fast is None) or (fast.next is None):
                return False
            fast = fast.next.next
            slow = slow.next
        return True