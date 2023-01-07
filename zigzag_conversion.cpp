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
    string convert(string s, int numRows) {
        if (numRows != 1) {
            int divisor = numRows*2-2;
            string ans = "";
            int i = 0; 
            while (i < s.length()) { //first line
                ans.append(1, s[i]);
                i+=divisor;
            }

            for (long k = 1; k < numRows-1; k++) { //in the middle 
              i=k;
              int x = 3;
              while (i < s.length()) {
                ans.append(1, s[i]);
                i = divisor*(x/2) - i%divisor;
                x++;
              }
            }

            i=numRows-1;
            while (i < s.length()) { //last line
                ans.append(1, s[i]);
                i+=divisor;
            }
          
            return ans;
        }
        return s;
    }
};
