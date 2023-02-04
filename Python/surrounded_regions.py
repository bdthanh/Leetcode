from typing import List
class Solution:
  def solve(self, board: List[List[str]]) -> None:
    m = len(board)
    n = len(board[0])
    visited = [[False for i in range(n)] for j in range(m)]
    if m <= 2 or n <= 2:
      return
    group = []
    def findGroup(a, b, group):
      isOnEdge = False
      if board[a][b] == 'O' and not visited[a][b]:
        visited[a][b] = True
        group.append([a,b])
        if a+1 != m:
          isOnEdge = findGroup(a+1, b, group) or isOnEdge
        if a-1 != -1:
          isOnEdge = findGroup(a-1, b, group) or isOnEdge
        if b+1 != n:
          isOnEdge = findGroup(a, b+1, group) or isOnEdge
        if b-1 != -1:
          isOnEdge = findGroup(a, b-1, group) or isOnEdge
        if a+1 == m or a-1 == -1 or b+1 == n or b-1 == -1:
          isOnEdge = True
      return isOnEdge
      
    for a in range(m):
      for b in range(n):
        if board[a][b] == 'X':
          visited[a][b] = True
          continue
        if board[a][b] == 'O' and visited[a][b] == True:
          continue
        isOnEdge = findGroup(a, b, group)
        if isOnEdge:
          group = []
          isOnEdge = False
        else:
          while len(group) != 0:
            board[group[-1][0]][group[-1][1]] = 'X'
            group.pop()
        

board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
for i in board:
  print(i)
Solution().solve(board)
print("------------------------------")
for i in board:
  print(i)
print("------------------------------")
board = [["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]
for i in board:
  print(i)