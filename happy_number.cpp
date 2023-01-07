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
class Solution {
public:
    int findNew(int x) {
        vector<int> digits;
        while (x!=0) {
          int digit = x%10;
          x/=10;
          digits.push_back(digit);
        }
        int num = 0;
        for (auto &x: digits) {
          num += x*x;
        }
        return num;
    }
    bool isHappy(int n) {
        unordered_set<int> set;
        while (set.find(n) == set.end()) {
            set.insert(n);
            n = findNew(n);
            if (n == 1) return true;
        }
        return false;
    }
};