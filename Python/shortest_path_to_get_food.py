from typing import List
class Solution:
  def getFood(self, grid: List[List[str]]) -> int:
    m = len(grid)
    n = len(grid[0])
    directions = [[1,0],[0,1],[-1,0],[0,-1]] 
  
    start = None
    for i in range(m):
      for j in range(n):
        if grid[i][j] == "*":
          start = [i,j]
    queue = []
    
    queue.append([start[0], start[1]])
    dist = 0
    while queue:
      for _ in range(len(queue)):
        row, col = queue.pop(0)
        if grid[nextRow][nextCol] == 'X':
          continue
        grid[row][col] = 'X' #visited
        for nextCell in directions:
          nextRow = row+nextCell[0]
          nextCol = col+nextCell[1]
          if 0 <= nextRow < m and 0 <= nextCol < n:
            if grid[nextRow][nextCol] == '#':
              return dist+1
            queue.append([nextRow, nextCol, ])
      dist+=1
    return -1
  
grid = [["#","O","#"],["O","*","O"],["#","O","#"]]
print(Solution().getFood(grid))
    