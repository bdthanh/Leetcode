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
    int maxProfit(vector<int>& prices) {
        int minSoFar = INT_MAX;
        int maxAns = 0;
        for (int i = 0 ; i < prices.size(); i++) {
            if (minSoFar > prices[i]) {
                minSoFar = prices[i];
            } else if (prices[i] - minSoFar > maxAns) {
                maxAns = prices[i] - minSoFar;
            }
        }
        return maxAns;
    }
};
