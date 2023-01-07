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
    int modifiedBinarySearch(vector<int>& nums, int begin, int end, int target) {
        if (begin == end) {
            if (nums[begin] != target) {
              return -1;
            } 
            else if (nums[begin] == target) {
              return begin;
            }
        } else {
            int mid = (begin + end)/2;
            if (nums[mid] == target) return mid;
            else if (nums[begin] <= nums[mid]) {
                if (nums[begin] <= target && target <= nums[mid]) {
                    return modifiedBinarySearch(nums, begin, mid, target);
                }
                return modifiedBinarySearch(nums, mid+1, end, target);
            } else if (nums[begin] >= nums[mid]) {
                if (nums[mid] <= target && target <= nums[end]) {
                    return modifiedBinarySearch(nums, mid, end, target);
                }
                return modifiedBinarySearch(nums, begin, mid, target);
            } 
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {
        int ans = modifiedBinarySearch(nums, 0, nums.size()-1, target);
        return ans;
    }
};