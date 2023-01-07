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
class Solution(object):
  def dfs(self, grid, r, c): 
    num_row = len(grid)
    num_col = len(grid[0])
    grid[r][c] = '0'
    if c + 1 < num_col and grid[r][c+1] == '1':
      self.dfs(grid, r, c+1)
    if r + 1 < num_row and grid[r+1][c] == '1':
      self.dfs(grid, r+1, c)
    if c - 1 >= 0 and grid[r][c-1] == '1':
      self.dfs(grid, r, c-1)
    if r - 1 >= 0 and grid[r-1][c] == '1': 
      self.dfs(grid, r-1, c)
  
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    num_islands = 0
    num_row = len(grid)
    num_col = len(grid[0])
    for r in range(num_row): 
      for c in range(num_col):
        if grid[r][c] == '1':
          self.dfs(grid, r, c)
          num_islands += 1
    return num_islands