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
  int lengthOfLongestSubstring(string s) {
    int list[256];
    int ans = 0;
    int checkpoint = -1;
    for (int i = 0; i < 256; i++) {
      list[i] = -1;
    }
    for (int i = 0; i < s.length(); i++) {
      if (list[(int) s[i]] != -1) {
        checkpoint = max(checkpoint, list[(int) s[i]]);
      } 
      ans = max(ans, i - checkpoint);
      list[(int) s[i]] = i;
    }
    return ans;
  }
};