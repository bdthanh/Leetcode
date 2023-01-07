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
    int maxOperations(vector<int>& nums, int k) {
        list<int> num;
        for (long i = 0; i < nums.size(); i++) {
            num.push_back(nums[i]);
        }
        unordered_map<int, list<list<int>::iterator>> map;
        std::list<int>::iterator it = num.begin();
        long ans = 0;
        for (long i = 0; i < nums.size();i++) {
            if (nums[i] > k) {
                it++;
                continue;
            }
            if (map.find(k - nums[i]) == map.end()) {
                if (map.find(nums[i]) == map.end()) {
                    list<list<int>::iterator> li;
                    li.push_back(it);
                    map[nums[i]] = li;
                } else {
                    auto find = map.find(nums[i]);
                    find->second.push_back(it);
                }
            } else {
                if (!map.find(k - nums[i])->second.empty()) {
                    auto find = map.find(k - nums[i]);
                    find->second.pop_front();
                    ans += 1;
                } else {
                    if (map.find(nums[i]) == map.end()) {
                        list<list<int>::iterator> li;
                        li.push_back(it);
                        map[nums[i]] = li;
                    } else {
                        auto find = map.find(nums[i]);
                        find->second.push_back(it);
                    }
                }
            }
            it++;
        }
        return ans;
    }
};