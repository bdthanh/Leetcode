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
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        long len = s.length();
        unordered_map<char, int> umap;
        for (long i = 0; i < len; i++) {
            auto it = umap.find(s[i]);
            if (it == umap.end()) {
                umap[s[i]] = 1;
            } else {
                it->second += 1;
            }
        }
        for (long i = 0; i < len; i++) {
            auto it = umap.find(t[i]);
            if (it == umap.end()) {
                return false;
            } else {
                it->second -= 1;
                if (it->second < 0) {
                    return false;
                }
            }
        }
        return true;
    }
};