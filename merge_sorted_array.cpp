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
    void insert(vector<int>& nums1, int insertID, int insertVal, int size) {
        for (long i = size-1; i > insertID; i--) {
            nums1[i] = nums1[i-1];
        }
        nums1[insertID] = insertVal;
    }
    
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0, j = 0;
        while (i < m || j < n) {
            if (j == n || (i < m && j < n && nums1[i] < nums2[j])) {
                i++;
            } else if (i == m || (i < m && j < n && nums1[i] >= nums2[j])) {
                m++;
                insert(nums1, i, nums2[j], m);
                j++;
            }
        }
        
    }
};