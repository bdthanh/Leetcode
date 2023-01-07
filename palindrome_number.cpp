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
    bool isPalindrome(int x) {
        if (x == 0) return true;
        if (x < 0 || x % 10 == 0) return false;
        long newX = 0;
        long oldX = x;
        while (oldX != 0) {
            newX *= 10;
            newX += oldX %10;
            oldX /= 10;
        }
        if (newX == x) return true;
        return false;
    }
};