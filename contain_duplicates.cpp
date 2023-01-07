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
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<long, bool> umap;
        for (long i = 0; i < nums.size(); i++) {
            auto it = umap.find(nums[i]);
            if (it != umap.end()) {
                return true;
            } else {
                umap[nums[i]] = true;
            }
        }
        return false;
    }
};