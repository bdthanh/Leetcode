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
    int romanToInt(string s) {
        int ans = 0;
        unordered_map<char, int> umap;
        umap['I'] = 1;
        umap['V'] = 5;
        umap['X'] = 10;
        umap['L'] = 50;
        umap['C'] = 100;
        umap['D'] = 500;
        umap['M'] = 1000;
        for (long i = 0; i < s.length(); i++) {
            if (i != s.length() - 1) {
                if (umap.find(s[i])->second < umap.find(s[i+1])->second) ans -= umap.find(s[i])->second;
                else ans += umap.find(s[i])->second;
            } else ans += umap.find(s[i])->second;
        }
        return ans;
    }
};