#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <numeric>
#include <queue>
#include <list>
#include <stack>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std; 

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* ans = new ListNode;
        ListNode* prev = ans;
        while (list1 != NULL || list2 != NULL) {
            if (list1 == NULL || (list1 != NULL && list2 != NULL && list1->val > list2->val)) {
                ListNode* cur = new ListNode(list2->val);
                list2 = list2->next;
                prev->next = cur;
                prev = cur;
            } else if (list2 == NULL || (list1 != NULL && list2 != NULL && list1->val <= list2->val)) {
                ListNode* cur = new ListNode(list1->val);
                list1 = list1->next;
                prev->next = cur;
                prev = cur;
            }
        }
        return ans->next;
    }
};