from math import sqrt
class Solution:
  def countDigits(self, num: int) -> int:
    numCopy = num
    count = 0
    while num != 0:
      digit = num%10
      num = int(num/10)
      if numCopy % digit == 0:
        count += 1
    return count
num = 7
print(Solution().countDigits(num))
      