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
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        vector<int> leftProduct, rightProduct;
        long left = 1, right = 1;
        for (int i = 0; i < nums.size(); i++) {
            leftProduct.push_back(left);
            left *= nums[i];
            rightProduct.push_back(right);
            right *= nums[nums.size() - i - 1];
        }
        for (int i = 0; i < nums.size(); i++) {
            answer.push_back(leftProduct[i] * rightProduct[nums.size() - i - 1]);
        }
        return answer;
    }
};     