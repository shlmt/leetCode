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
    int gcd(int a,int b){
        int tmp;
        while(b!=0){
            tmp = b;
            b = a%b;
            a=tmp;
        }
        return a;
    }

public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        auto prv=head, nxt=head->next;
        while(nxt){
            int gcd1 = gcd(prv->val,nxt->val);
            prv->next = new ListNode(gcd1, nxt);
            prv=nxt;
            nxt=nxt->next;
        }
        return head;
    }
};