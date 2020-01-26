class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        
        // iterative version
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;
        /*
        null 1->2->3->4->5->null
         p   c
        null<-1 2->3->4->5->null
              p c 
        null<-1<-2 3->4->5->null
                 p c 
        null<-1<-2<-3 4->5->null
                    p c
        null<-1<-2<-3<-4 5->null
                       p c
        null<-1<-2<-3<-4<-5 null
                          p c
        */
    }
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        //recursive version
        // n1 --> n2 --> ... nk --> nk+1 <--nk+2 <-- .... nend
        // what we want is nk-->next-->next(which is nk-1->next) = nk
        // make sure n1-> next need to point to null pointer! otherwise there will be a cycle
        if(head == nullptr || head->next == nullptr){
            return head;
        }
        ListNode* p = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return p;
    }
};

