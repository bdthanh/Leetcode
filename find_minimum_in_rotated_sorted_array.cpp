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
    int modifiedBinarySearch(vector<int>& nums, int begin, int end) {
        if (begin == end) {
            if (begin == 0) {
                if (nums[begin] <= nums[nums.size()-1]) return nums[begin];
            } else if (begin != 0) {
                if (nums[begin] < nums[begin-1]) return nums[begin];
            }
        } 
        int mid = (begin + end)/2;
        if (mid == begin) {
            if (nums[mid] < nums[mid + 1]) return nums[mid];
                else return nums[mid+1];
        } else {
            if (nums[begin] < nums[mid] && nums[mid] < nums[end]) return nums[begin];
            else if (nums[begin] < nums[mid] && nums[mid] > nums[end]) return modifiedBinarySearch(nums, mid, end);
        }
        return modifiedBinarySearch(nums, begin, mid);
    }

    int findMin(vector<int>& nums) {
        return modifiedBinarySearch(nums, 0, nums.size()-1); 
    }
};
//speed test
//speed test