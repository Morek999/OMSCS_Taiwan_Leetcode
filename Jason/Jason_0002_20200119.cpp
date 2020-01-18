/*
So this problem is actually more straight forward but my code is not very clean and efficient. I found the optimal solution and attach it in the end.
Here's my thought: first I check if there's nullptr in l1 or l2, if there is, just return the other one.
If all existent, then we need to loop through both list and do the summation. I defined a dummy node and this way when I finished the whole operation,
I just need to return dummy.next then I got the answer.
I use a while loop to iterate and the loop stop if one of the pointer is empty. During the iteration, I calculate the summation and carry to the next 
digit, and then create the next node equal to the sum.
If we jumped out of the loop, three possible condition: 
1. l1 finished
2. l2 finished
3. Both finished

If it's 1 or 2 just continue to loop through the rest of the list, if it's 3 then simply check if there's carry and create next node if there is a carry.

Time complexity : O(max(n,m)) since the longer list will determine how many components we need to visit
Space complexity: O(max(n,m)) same reason as above
*/
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr){
            return l2;
        }
        if(l2 == nullptr){
            return l1;
        }
        int sum = 0, carry = 0;
        ListNode* dummy = new ListNode(0);
        ListNode* p = dummy;
        
        while(l1 != nullptr && l2 != nullptr){
            sum = carry + l1 -> val + l2 -> val;
            if(sum >= 10){
                sum = sum % 10;
                carry = 1;
            }
            else{
                carry = 0;
            }
            p->next = new ListNode(sum);
            p = p->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        if(l1 != nullptr){
            while(l1 != nullptr){
                sum = carry + l1->val;
                if(sum >= 10){
                    sum = sum % 10;
                    carry = 1;
                }
                else{
                    carry = 0;
                }
                p->next = new ListNode(sum);
                p = p->next;
                l1 = l1->next;
            }
        }
        else if(l2 != nullptr){
            while(l2 != nullptr){
                sum = carry + l2->val;
                if(sum >= 10){
                    sum = sum % 10;
                    carry = 1;
                }
                else{
                    carry = 0;
                }
                p->next = new ListNode(sum);
                p = p->next;
                l2 = l2->next;
            }
        }
        if(carry == 1){
            p->next = new ListNode(carry);
        }
        return dummy->next;
    }
};

/*
The optimal solution works way more elegantly.....
Reference: https://www.youtube.com/watch?v=-UBiYuIVErM&
*/

class Solution {
public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    int sum = 0;
    while (l1 || l2 || sum) {
      sum += (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
      l1 = l1 ? l1->next : nullptr;
      l2 = l2 ? l2->next : nullptr;
      tail->next = new ListNode(sum % 10);
      sum /= 10;
      tail = tail->next;
    }            
    return dummy.next;
  }
};