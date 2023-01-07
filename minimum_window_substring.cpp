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
    string minWindow(string s, string t) {
        map<char,int> map;
        for(int i=0;i<t.size();i++){
            map[t[i]]++;
        }
        int count = map.size();
        int i=0;
        int j=0;
        string ans = "";
        int ans_size=INT_MAX;
        if(s.size()<t.size()){
            return "";
        }
        while(j<s.size()){
            if(map.find(s[j])!=map.end()){
                 map[s[j]]--;
                 if(map[s[j]]==0){
                     count--;
                 }
            }
            if(count==0){
              while(true){
                auto it=map.find(s[i]);
                if(it!=map.end()){
                     map[s[i]]++;
                     if(map[s[i]]==1 ){
                        if(ans_size>j-i+1){
                          ans=s.substr(i,j-i+1);
                          ans_size=j-i+1;   
                        }
                        i++;
                        count++;
                        break;

                    }

                    i++;
                } else {
                    i++;
                }
              }    
            }
            j++;
        }
        return ans;
 }
};