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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 1;
        auto it1 = head; 
        auto it2 = head; 
        while (it1->next != NULL) {
          size += 1;
          it1 = it1->next;
        }
        auto prev = it2;
        for (int i = 0; i < size - n; i++) {
          prev = it2;
          it2 = it2->next; 
        }
        if (it2->next != NULL) {
          auto aft = it2->next;
          prev->next=aft;
        }
        if (it2->next == NULL) {
            prev->next = NULL;
        }
        if (it2 == head) {
            if (it2->next == NULL) return NULL;
            else {
                head = head->next;
            }
        }
        
        return head;
    }
};