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
    string longestCommonPrefix(vector<string>& strs) {
      string ans = "";
      for (long i = 0; i < strs[0].length(); i++) {
        bool isSame = true;
        for (long j = 0; j < strs.size(); j++) {
          if (i + 1 > strs[j].length()) {
            isSame = false;
          } else if (strs[0][i] != strs[j][i]) {
            isSame = false;
          }
        }
        if (isSame) {
          ans.append(1, strs[0][i]);
        } else {
          return ans;
        }
      }
      return ans;
    }
};