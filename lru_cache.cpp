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
class LRUCache {
public:
    list<pair<int,int>> li;
    unordered_map<int, list<pair<int,int>>::iterator> umap;
    int capacity;
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto it = umap.find(key);
        if (it != umap.end()) {
            auto pair = *(it->second);
            li.erase(it->second);
            li.push_front(pair);
            umap[key] = li.begin();
            return pair.second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if (umap.find(key) == umap.end() && umap.size() == capacity) {
            int evictedKey = li.back().first;
            if (li.size() != 0) {
                li.pop_back();
            }
            umap.erase(evictedKey);
            li.push_front(make_pair(key,value));
            umap[key] = li.begin();
        } else if (umap.find(key) == umap.end() && umap.size() != capacity) {
            li.push_front(make_pair(key,value));
            umap[key] = li.begin();
        } else {
            auto it = umap.find(key);
            li.erase(it->second);
            li.push_front(make_pair(key,value));
            umap[key] = li.begin();
        } 
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    LRUCache lRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1}
    lRUCache.put(2, 2); // cache is {1=1, 2=2}
    cout << lRUCache.get(1);    // return 1
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    cout << lRUCache.get(2);    // returns -1 (not found)
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    cout << lRUCache.get(1);    // return -1 (not found)
    cout << lRUCache.get(3);    // return 3
    cout << lRUCache.get(4);    // return 4
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */