""" 
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        ptA = headA
        ptB = headB
        
        while ptA is not ptB:
            ptA = headB if ptA is None else ptA.next
            ptB = headA if ptB is None else ptB.next
        
        return ptA