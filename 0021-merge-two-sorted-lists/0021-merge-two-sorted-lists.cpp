/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        while(list1 && list2){
            int val1 = list1->val, val2 = list2->val;
            if(val1<val2){
                tail->next = new ListNode(val1);
                list1 = list1->next;
            }
            else{
                tail->next = new ListNode(val2);
                list2 = list2->next;
            }
            tail = tail->next;
       }
        if(list1) tail->next = list1;
        else if(list2) tail->next = list2;
        return dummy.next;
    }
};