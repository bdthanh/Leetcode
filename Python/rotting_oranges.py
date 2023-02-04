from typing import List
class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    stack = []
    m = len(grid)
    n = len(grid[0])
    countNormalOrange = 0
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    time = 0
    for row in range(m):
      for col in range(n):
        if grid[row][col] == 2:
          stack.append([row, col])
        if grid[row][col] == 1:
          countNormalOrange +=1
    if len(stack) == 0 and countNormalOrange != 0:
      return 0 
    while len(stack) != 0:
      newStack = []
      while len(stack) != 0:
        curOrange = stack.pop()
        for dir in dirs:
          nextRow, nextCol = curOrange[0] + dir[0], curOrange[1] + dir[1]
          if -1 < nextRow < m and -1 < nextCol < n and grid[nextRow][nextCol] == 1:
            countNormalOrange -= 1
            grid[nextRow][nextCol] = 2 # visited
            newStack.append([nextRow, nextCol])  
      stack = newStack
      time+=1
    if countNormalOrange != 0:
      return -1
    return time-1
  
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))
    