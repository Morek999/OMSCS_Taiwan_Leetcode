""" 
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
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
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None: return True
        half1 = self.end_half1(head)
        half2 = self.reverse_list(half1.next)
        result = True
        p1 = head
        p2 = half2
        while result and p2 is not None:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next
        half1.next = self.reverse_list(half2)
        return result

    def end_half1(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev