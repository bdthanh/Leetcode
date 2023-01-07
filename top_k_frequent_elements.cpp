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
struct CustomCompare {
    bool operator() (const pair<int, int> &a, const pair<int, int> &b) const {
        return a.first < b.first;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> umap;
        for (int i = 0; i < nums.size();i++) {
          auto it = umap.find(nums[i]);
          if (it == umap.end()) umap[nums[i]] = 1;
          else it->second+=1;
        }
        vector<pair<int,int>> vec;
        for (auto &x: umap) {
          vec.push_back({x.second,x.first});
        }
        sort(vec.begin(),vec.end(), CustomCompare());
        vector<int> ans;
        for (int i = 0; i < k; i++) {
          ans.push_back(vec[vec.size()-1-i].second);
        }
        return ans;
    }
};