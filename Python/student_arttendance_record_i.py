class Solution:
  def checkRecord(self, s: str) -> bool:
    countA = 0
    countLConsecutive = 0
    for char in s:
      if char == 'A':
        countA+=1
        countLConsecutive = 0
        if countA >= 2:
          return False
      elif char == 'L':
        countLConsecutive+=1
        if countLConsecutive >= 3:
          return False
      else:
        countLConsecutive = 0
    return True
          
      