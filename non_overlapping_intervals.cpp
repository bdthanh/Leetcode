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
  bool operator() (const vector<int> &a, const vector<int> &b) const {
        return a[1]<b[1];
    }
};
class Solution {
  
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
         if (intervals.size()==1) return 0;
        sort(intervals.begin(),intervals.end(), CustomCompare());
        int prevend=intervals[0][1];
        int count=0;
        for(int i=1;i<intervals.size();i++)
        {
            if(intervals[i][0]<prevend)count++;
            else{
                prevend=intervals[i][1];
            }
        }
        return count;
    }
};