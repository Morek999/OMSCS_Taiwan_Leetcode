""" 
148. Sort List
https://leetcode.com/problems/sort-list/
Time complexity: O()
Space complexity: O()
 """

from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next 
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next: return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        return self.merge(self.sortList(head), self.sortList(slow))