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
    ListNode* mergeNodes(ListNode* head) {
        ListNode dummy(0);
        ListNode* list = &dummy;
        int num=0;
        for(auto node=head->next; node; node=node->next){
            if(node->val!=0) num+=node->val;
            else{
                list->next = new ListNode(num);
                list=list->next;
                num=0;
            }
        }
        return dummy.next;
    }
};