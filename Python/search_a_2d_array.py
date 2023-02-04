from typing import List
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def binarySearchRow(beg: int, end: int) -> int:
      if beg == end:
        if beg == 0 and matrix[0][0] > target:
          return -1
        return beg
      mid = int((beg+end)/2)
      if matrix[mid+1][0] > target:
        return binarySearchRow(beg, mid)
      return binarySearchRow(mid+1, end)
    
    
    def binarySearchCol(beg: int, end: int, row: int) -> int:
      if beg == end: 
        if matrix[row][beg] == target:
          return beg
        else:
          return -1
      mid = int((beg+end)/2)
      if matrix[row][mid] >= target:
        return binarySearchCol(beg, mid, row)
      return binarySearchCol(mid+1, end, row)
    
    row = binarySearchRow(0, len(matrix)-1)
    if row == -1: 
      return False
    col = binarySearchCol(0, len(matrix[0])-1, row)
    if col == -1:
      return False
    return True  
  
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3  
print(Solution().searchMatrix(matrix, target))