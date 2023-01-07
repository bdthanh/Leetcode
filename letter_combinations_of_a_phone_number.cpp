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
    vector<string> letterCombinations(string digits) {
        vector<string> vec;
        int len = digits.length();
        vector<vector<string>> table {{"a","b","c"},{"d","e","f"},{"g","h","i"},{"j","k","l"},{"m","n","o"},{"p","q","r","s"},{"t","u","v"},{"w","x","y","z"}};
        string str = ""; 
        for (long a = 0; digits.length() >=1 && a < table[(int)digits[0]-50].size() ; a++) {
            str.append(table[(int)digits[0]-50][a]);
            if (len == 1) {
                vec.push_back(str);
            }
            for (long b = 0; digits.length() >=2 && b < table[(int)digits[1]-50].size() ; b++) {
                str.append(table[(int)digits[1]-50][b]);
                if (len == 2) {
                    vec.push_back(str);
                }
                for (long c = 0; digits.length() >=3 && c < table[(int)digits[2]-50].size() ; c++) {
                    str.append(table[(int)digits[2]-50][c]);
                    if (len == 3) {
                        vec.push_back(str);
                    }
                    for (long d = 0; digits.length() >=4 && d < table[(int)digits[3]-50].size() ; d++) {
                        str.append(table[(int)digits[3]-50][d]);
                        vec.push_back(str);
                        str = str.substr(0,str.length()-1);
                    }
                    str = str.substr(0,str.length()-1);
                }
                str = str.substr(0,str.length()-1);
            }
            str = str.substr(0,str.length()-1);
        }
        return vec;
    }
};