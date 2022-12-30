class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    # check row
    for i in range(9):
      seenRow = set()
      for j in range(9):
        if board[i][j] != ".": 
          if board[i][j] in seenRow:
            return False
          seenRow.add(board[i][j]) 
          
      seenCol = set()
      for j in range(9):
        if board[j][i] != ".": 
          if board[j][i] in seenCol:
            return False
          seenCol.add(board[j][i]) 
    
    # check square
    for i in range(0,9,3):
      for j in range(0,9,3):
        seen = set()
        for x in range(i, i+3):
          for y in range(j, j+3):
            if board[i][j] != ".": 
              if board[i][j] in seen:
                return False
            seen.add(cell) 
    return True
            
    
            
        