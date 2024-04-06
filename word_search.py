from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(board, i, j, cur_char: int = 0):
            if i < 0 or i >= height or j < 0 or j >= width or board[i][j] != word[cur_char]:
                return False
            
            if cur_char == len(word) - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = '*'
            res = dfs(board, i + 1, j, cur_char + 1) or dfs(board, i - 1, j, cur_char + 1) or dfs(board, i, j + 1, cur_char + 1) or dfs(board, i, j - 1, cur_char + 1)
            board[i][j] = temp
            
            return res
            

        for i in range(height):
            for j in range(width):
                if dfs(board, i, j, 0):
                    return True
        return False