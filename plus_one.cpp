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
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size()-1;
        while (i != -1 && digits[i]+1==10) {
          digits[i] = 0;
          i--;
        }
        if (i != -1) {
          digits[i] += 1;
        } else {
          digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};