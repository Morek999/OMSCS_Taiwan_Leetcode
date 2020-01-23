""" 
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        multi = 1
        l = len(lists)
        while multi < l:
            for i in range(0, (l - multi), (multi * 2)):
                lists[i] = self.merge2(lists[i], lists[i + multi])
            multi *= 2
        return lists[0] if l > 0 else lists
        
    def merge2(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        if not l2:
            point.next = l1
        return head.next

LN = [
    [1,4,5],
    [1,3,4],
    [2,6]
]

ans = []
for i in range(len(LN)):
    ans.append(ListNode(LN[i][0]))
    tmp = ans[-1]
    for j in range(1, len(LN[i])):
        tmp.next = ListNode(LN[i][j])
        tmp = tmp.next

for trails in ans:
    print(Solution().mergeKLists(trails))
