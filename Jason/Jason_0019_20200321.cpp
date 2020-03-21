/*
First thought I used two pass algorithm, which is first traverse all of the list and get the length of list, then use the length - n to
get the position to remove the node. Using dummy node will make the second pass operation easier.
The one pass algorithm can be achieved by using two pointers, and the two pointers are separated by n nodes.
Every time we just shift both pointers by one node, then once the first node reach null pointer, the second pointer is in front of the node
that we want to delete. Just delete it and return dummy->next

Time complexity: O(n)
Space complexity: O(1)
 */
// One pass
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == nullptr){
            return nullptr;
        }
        ListNode* dummy = new ListNode;
        dummy -> next = head;
        ListNode* first = dummy;
        ListNode* second = dummy;
        // set two pointers n nodes apart, need to shift n+1 times
        for(int i = 0; i <= n; i++){
            first = first->next;
        }
        while(first){
            first = first->next;
            second = second->next;
        }
        second->next = second->next->next;
        return dummy->next;
    }
};

// Two pass
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == nullptr){
            return nullptr;
        }
        ListNode* dummy = new ListNode;
        dummy -> next = head;
        ListNode* p = head;
        int l = 0;
        while(p){
            l++;
            p = p->next;
        } 
        int pos = l - n;
        p = dummy;
        while(pos > 0){
            p = p->next;
            pos--;
        }
        p->next = p->next->next;
        return dummy->next;
    }
};