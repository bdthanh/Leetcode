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
    string countAndSay(int n) {
        if (n == 1) return "1";
        string s = countAndSay(n - 1);
        int cnt = 1;
        char now = s[0];
        string ans = "";
        for (int i = 1; i < s.length();i++) {
            if (s[i] == now) {
                cnt++;
                continue;
            }
            ans += to_string(cnt) + now;
            cnt = 1;
            now = s[i];
        }
        ans += to_string(cnt) + now;
        return ans;
    }
};