// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head != nullptr) {
            head->val = 100001;
            head = head->next;
        }
        while (head != nullptr) {
           if (head->val == 100001) return true; 
           head->val = 100001;
           head = head->next;
        }
        return false;
    }
};