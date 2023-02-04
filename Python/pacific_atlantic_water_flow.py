from typing import List
class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    # pass 1: 
    # all heights are adjacent to Pacific Ocean
    visited1 = set()
    stack1 = []
    for col in range(n):
      stack1.append([0,col])
      visited1.add(tuple([0,col]))
    for row in range(1,m):
      stack1.append([row,0])
      visited1.add(tuple([row,0]))
    while len(stack1) != 0:
      [row, col] = stack1.pop()
      for dir in dirs:
        nextRow = row + dir[0]
        nextCol = col + dir[1]
        if -1 < nextRow < m and -1 < nextCol < n and heights[row][col] <= heights[nextRow][nextCol] and not tuple([nextRow, nextCol]) in visited1:
          visited1.add(tuple([nextRow,nextCol]))
          stack1.append([nextRow, nextCol])
    # pass 2: 
    # all heights are adjacent to Atlantic Ocean
    visited2 = set()
    stack2 = []
    for col in range(n):
      stack2.append([m-1,col])
      visited2.add(tuple([m-1,col]))
    for row in range(0,m-1):
      stack2.append([row,n-1])
      visited2.add(tuple([row,n-1]))
    while len(stack2) != 0:
      [row, col] = stack2.pop()
      for dir in dirs:
        nextRow = row + dir[0]
        nextCol = col + dir[1]
        if -1 < nextRow < m and -1 < nextCol < n and heights[row][col] <= heights[nextRow][nextCol] and not tuple([nextRow, nextCol]) in visited2:
          visited2.add(tuple([nextRow,nextCol]))
          stack2.append([nextRow, nextCol])
    ans = []
    for height in visited1:
      if height in visited2:
        ans.append(height)
    return ans
  
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
heights2 = [[2,1],[1,2]]
print(Solution().pacificAtlantic(heights2))